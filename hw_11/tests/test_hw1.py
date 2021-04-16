from hw_11.hw1 import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")

def test_SimplifiedEnum():
    assert ColorsEnum.RED == "RED"
    assert ColorsEnum.BLUE == "BLUE"
    assert ColorsEnum.ORANGE == "ORANGE"
    assert ColorsEnum.BLACK == "BLACK"

