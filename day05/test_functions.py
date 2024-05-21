import pytest

from count_functions import count_characters, count_lines, count_words

def test_count_characters():
    assert count_characters("Hello, World!") == 13
    assert count_characters("") == 0
    assert count_characters("12345\n67890") == 11

def test_count_lines():
    assert count_lines("Hello\nWorld") == 2
    assert count_lines("One line") == 1
    assert count_lines("Hi\nmy name\nis\nMaher") == 4

def test_count_words():
    assert count_words("Hello, World!") == 2
    assert count_words("Hi My name is Maher") == 5
    assert count_words("   ") == 0
    assert count_words("") == 0