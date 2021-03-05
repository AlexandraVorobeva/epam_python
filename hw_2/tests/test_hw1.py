import os

from hw_2.hw1 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
    open_file,
)

import pytest


@pytest.fixture()
def file_test_open():
    filename = "file_test_open.txt"
    with open(filename, "w") as f:
        f.write(
            "Der Waldgang \\u2014 es ist keine Idylle, die sich hinter dem Titel verbirgt. "
        )
    yield filename
    os.remove(filename)


def test_open_file(file_test_open):
    actual_result = open_file(file_test_open)

    assert (
        actual_result
        == "Der Waldgang \u2014 es ist keine Idylle, die sich hinter dem Titel verbirgt. "
    )


@pytest.fixture()
def file_with_diverse_words():
    filename = "file_with_diverse_words.txt"
    with open(filename, "w") as f:
        f.write(
            "F\\u00e4lle abcd abcde aaaaaaaaaaaaaaaaaaaa abcdef abcdefg"
            " abcdefgh abcdefghi  abcdefghij abcdefghijk abcdefghijkl"
        )
    yield filename
    os.remove(filename)


def test_get_longest_diverse_words(file_with_diverse_words):
    actual_result = get_longest_diverse_words(file_with_diverse_words)

    assert actual_result == [
        "abcdefghijkl",
        "abcdefghijk",
        "abcdefghij",
        "abcdefghi",
        "abcdefgh",
        "abcdefg",
        "abcdef",
        "abcde",
        "F\u00e4lle",
        "abcd",
    ]


@pytest.fixture()
def file_with_rarest_char():
    filename = "file_with_rarest_char.txt"
    with open(filename, "w") as f:
        f.write("madam I'm Adam")
    yield filename
    os.remove(filename)


def test_get_rarest_char(file_with_rarest_char):
    actual_result = get_rarest_char(file_with_rarest_char)

    assert actual_result == "I"


@pytest.fixture()
def file_with_punctuation():
    filename = "file_with_rarest_char.txt"
    with open(filename, "w") as f:
        f.write(
            "Hundert  Prozent:  das  ist  die  ideale  Ziffer,  die,  wie  alle Ideale, stets unerreichbar bleibt. "
        )
    yield filename
    os.remove(filename)


def test_count_punctuation_chars(file_with_punctuation):
    actual_result = count_punctuation_chars(file_with_punctuation)

    assert actual_result == 5


@pytest.fixture()
def file_with_non_ascii_chars():
    filename = "file_with_non_ascii_chars.txt"
    with open(filename, "w") as f:
        f.write(
            """
             Der Waldgang \\u2014 es ist keine Idylle, die sich hinter dem Titel verbirgt.
             Der  Leser  mu\\u00df  sich  vielmehr  auf  einen  bedenkli- chen Ausflug gefa\\u00dft machen,
             der nicht nur \\u00fcber vorgebahnte Pfade, sondern auch \\u00fcber die Grenzen der Betrachtung
             hin- ausf\\u00fchren wird."""
        )
    yield filename
    os.remove(filename)


def test_count_non_ascii_chars(file_with_non_ascii_chars):
    actual_result = count_non_ascii_chars(file_with_non_ascii_chars)

    assert actual_result == 6


def test_get_most_common_non_ascii_char(file_with_non_ascii_chars):
    actual_result = get_most_common_non_ascii_char(file_with_non_ascii_chars)

    assert actual_result == "\u00fc"