import asyncio
from decimal import Decimal
from heapq import nlargest, nsmallest
import aiohttp
from bs4 import BeautifulSoup
from collections import defaultdict
import simplejson as json


BASE_URL = "https://markets.businessinsider.com/"
COMPANY_STOCK_DATA = defaultdict(dict)


async def fetch_page_content(url: str) -> str:
    """Create connection and take html code"""
    semaphore = asyncio.Semaphore(100)
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=False) as response:
                return await response.text()


async def create_soup_object(url: str):
    """This function creates soup object"""
    page = await fetch_page_content(url)
    soup = BeautifulSoup(page, "lxml")
    return soup


async def fetch_number_of_pages() -> int:
    """Get number of pages with companies tables"""
    start_page = f"{BASE_URL}index/components/s&p_500"
    page = await create_soup_object(start_page)
    pages = page.find("div", class_="finando_paging").find_all("a")
    return int(pages[-1].text)


async def fetch_rub_usd_rate() -> Decimal:
    """Cheking rub-usd exchange rate"""
    url_cbr = "http://www.cbr.ru/scripts/XML_daily.asp"
    page = await create_soup_object(url_cbr)
    exchange_rate = page.find(id="R01235").find_next("value").get_text()
    return Decimal(exchange_rate.replace(",", "."))


async def save_parsed_company_page(url: str):
    """Save all parsed company pages into one list"""
    parsed_company_pages = []
    soup = await create_soup_object(url)
    parsed_company_pages.append(soup)
    return await fetch_sp500_additional_data(parsed_company_pages, url)


async def fetch_sp500_companies_info(number_of_page: int):
    """Collect information of all companies from table pages into dictionaries"""
    tasks = []
    all_url = f"{BASE_URL}index/components/s&p_500 ?p={number_of_page}"
    soup = await create_soup_object(all_url)
    table_of_companies = soup.find(class_="table table-small").find_all("a")
    for row in table_of_companies:
        company_url = "https://markets.businessinsider.com" + row["href"]
        growth_element = row.findParent().findParent().find_all("span")[-2]
        if growth_element is None:
            growth = 0
        else:
            growth = float(growth_element.text.replace(",", ""))
        COMPANY_STOCK_DATA[company_url]["growth"] = growth
        company_name = row["title"]
        COMPANY_STOCK_DATA[company_url]["name"] = company_name
        tasks.append(save_parsed_company_page(company_url))
    await asyncio.gather(*tasks)


def get_price(soup) -> Decimal:
    """Find value of company price in USD in script code"""
    price_element = soup.find(class_="price-section__current-value")
    price_in_usd = Decimal(price_element.text.replace(",", ""))
    return price_in_usd


def get_p_e_value(soup) -> float:
    """Find value of company P/E in script code"""
    pe_element = (
        soup.find("div", class_="snapshot")
        .find_all(class_="snapshot__data-item")[6]
        .text.split()[0]
    )
    pe_value = float(pe_element.replace(",", ""))
    if pe_value is None:
        pe_value = 0
    return pe_value


def get_potential_profit(soup) -> float:
    """Find 52 weeks lowest and highest value in script code"""
    week_high_element = soup.find(class_="snapshot__header", text="52 Week High")
    week_low_element = soup.find(class_="snapshot__header", text="52 Week Low")
    if week_low_element is None and week_high_element is None:
        profit = 0
    else:
        week_high_value = week_high_element.findParent().text.split()[0]
        week_high = float(week_high_value.replace(",", ""))

        week_low_value = week_low_element.findParent().text.split()[0]
        week_low = float(week_low_value.replace(",", ""))
        potential_profit = week_high / week_low

        profit = round(potential_profit, 2)
    return profit


async def fetch_sp500_additional_data(parsed_company_pages, company_url: str) -> dict:
    """In script code find additional information about companies:
    - code
    - stock price
    - profit
    - P/E
    """
    rub_usd_rate = await fetch_rub_usd_rate()
    for company in parsed_company_pages:
        preparing_company_data = COMPANY_STOCK_DATA[company_url]

        company_code_element = company.findChild(class_="price-section__category")
        preparing_company_data["code"] = company_code_element.span.text[2:]

        price_usd = get_price(company)
        price_rub = price_usd * rub_usd_rate
        preparing_company_data["price"] = price_rub

        pe = get_p_e_value(company)
        preparing_company_data["P/E"] = pe

        potential_profit = get_potential_profit(company)
        preparing_company_data["profit"] = potential_profit
        return preparing_company_data


def save_to_json(filename: str, value_name: str, data: list) -> None:
    """Saving information to JSON file"""
    with open(filename + ".json", "w") as file:
        top_10 = [
            {
                "name": data[i]["name"],
                "code": data[i]["code"],
                f"{value_name}": data[i][value_name],
            }
            for i in range(10)
        ]
        json.dump(top_10, file, indent=4)


async def main() -> None:
    """Starting point.
    Find information about S&P500 companies.
    Do it fast because of async method.
    """
    number_of_pages = await fetch_number_of_pages()
    for page in range(1, number_of_pages + 1):
        await fetch_sp500_companies_info(page)
        await asyncio.sleep(0.05)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    save_to_json(
        "growth",
        "growth",
        nlargest(10, COMPANY_STOCK_DATA.values(), key=lambda x: x["growth"])
    )
    save_to_json(
        "price",
        "price",
        nlargest(10, COMPANY_STOCK_DATA.values(), key=lambda x: x['price'])
    )
    save_to_json(
        "p_e",
        "P/E",
        nsmallest(10, COMPANY_STOCK_DATA.values(), key=lambda x: x["P/E"])
    )
    save_to_json(
        "profit",
        "profit",
        nlargest(10, COMPANY_STOCK_DATA.values(), key=lambda x: x["profit"])
    )
