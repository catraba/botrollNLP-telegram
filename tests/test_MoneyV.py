import pytest

from MoneyV import MoneyV



def test_type():
    assert type(MoneyV('bitcoin').extract_price()) == str


def test_start_with_dolar():
    value = MoneyV('bitcoin').extract_price()

    assert value[0] == '$'