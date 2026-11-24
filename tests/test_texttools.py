import pytest

from texttools import slugify, truncate, word_count


def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"


def test_slugify_collapses_separators():
    assert slugify("  Hello,  World! ") == "hello-world"


def test_word_count():
    assert word_count("one two  three") == 3
    assert word_count("") == 0


def test_truncate_short_text_unchanged():
    assert truncate("abc", 5) == "abc"


def test_truncate_long_text():
    assert truncate("abcdefghij", 7) == "abcd..."


def test_truncate_negative_limit():
    with pytest.raises(ValueError):
        truncate("abc", -1)
