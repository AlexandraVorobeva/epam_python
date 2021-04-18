import asynctest
import pytest
from hw_10.parser import *
import hw_10.parser


@pytest.fixture
def fake_create_soup_object():
    with open("test_data_01.html") as file:
        return file.read()


def test_get_price(fake_create_soup_object):
    expected_result = Decimal('2375.00')
    soup = BeautifulSoup(fake_create_soup_object, "lxml")
    actual_result = get_price(soup)
    assert expected_result == actual_result


def test_get_p_e_value(fake_create_soup_object):
    expected_result = 30.0
    soup = BeautifulSoup(fake_create_soup_object, "lxml")
    actual_result = get_p_e_value(soup)
    assert expected_result == actual_result


def test_get_potential_profit(fake_create_soup_object):
    expected_result = 1.88
    soup = BeautifulSoup(fake_create_soup_object, "lxml")
    actual_result = get_potential_profit(soup)
    assert expected_result == actual_result

