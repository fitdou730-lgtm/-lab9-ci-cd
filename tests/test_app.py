
from app import greeting, add_numbers


def test_greeting():
    assert greeting("Студент") == "Привет, Студент!"


def test_add_positive_numbers():
    assert add_numbers(5, 3) == 8


def test_add_negative_numbers():
    assert add_numbers(-5, 2) == -3
