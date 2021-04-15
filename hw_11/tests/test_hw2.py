from hw_11.hw2 import ElderDiscount, MorningDiscount, Order


def test_Order_with_different_discounts():
    morning_discount = MorningDiscount()
    elder_discount = ElderDiscount()
    order_1 = Order(100, morning_discount)
    order_2 = Order(100, elder_discount)

    assert order_1.final_price() == 50
    assert order_2.final_price() == 10

