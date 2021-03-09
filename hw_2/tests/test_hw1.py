import os

import pytest


from hw_2.hw1 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char
)


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (os.path.join(os.path.dirname(__file__), "data.txt"),
            [
                "unmißverständliche",
                "Bevölkerungsabschub",
                "Kollektivschuldiger",
                "Werkstättenlandschaft",
                "Schicksalsfiguren",
                "Selbstverständlich",
                "Fingerabdrucks",
                "Friedensabstimmung",
                "außenpolitisch",
                "Seinsverdichtungen",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(value: str, expected_result: str):
    actual_result = get_longest_diverse_words(value)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (os.path.join(os.path.dirname(__file__), "data.txt"), "› ‹ Y î ’ X"),
    ],
)
def test_get_rarest_char(value: str, expected_result: str):
    actual_result = get_rarest_char(value)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (os.path.join(os.path.dirname(__file__), "data.txt"), 5305),
    ],
)
def test_count_punctuation_chars(value: str, expected_result: int):
    actual_result = count_punctuation_chars(value)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (os.path.join(os.path.dirname(__file__), "data.txt"), 2972),
    ],
)
def test_count_non_ascii_chars(value: str, expected_result: int):
    actual_result = count_non_ascii_chars(value)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (os.path.join(os.path.dirname(__file__), "data.txt"), "ä"),
    ],
)
def test_get_most_common_non_ascii_char(value: str, expected_result: str):
    actual_result = get_most_common_non_ascii_char(value)
    assert actual_result == expected_result
