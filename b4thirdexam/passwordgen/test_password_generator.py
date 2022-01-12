import pytest
from passwordgenerator import (
    make_digits,
    pick_words_to_password,
    create_password,
    create_passwords
)
from pytest import MonkeyPatch

from passwordgenerator_exceptions import LenghtMustBeAnInteger


def test_create_password(monkeypatch: MonkeyPatch):
    def monkey_make_digits(p):
        return '11'
    monkeypatch.setattr('passwordgenerator.make_digits', monkey_make_digits)
    assert create_password('$', 2, '#', 1, ['git', 'gut']) == '#11$git$gut$11#'


def test_make_digits(monkeypatch: MonkeyPatch):
    def monkey_randint(p, f):
        return 1
    monkeypatch.setattr('passwordgenerator.randint', monkey_randint)
    assert make_digits(5) == '11111'


def test_pick_words_lenght_not_int():
    with pytest.raises(LenghtMustBeAnInteger):
        pick_words_to_password('b4thirdexam/words.txt', 3, 2, 'g')