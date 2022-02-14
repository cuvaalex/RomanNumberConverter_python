import pytest


def print_num(number):
    str_num = ""
    for i in range(1,number+1):
        str_num += str(i)
    return str_num


def test_return_one():
    result = print_num(1)
    assert result == "1"

def test_when_2_return_12():
    result = print_num(2)
    assert result == "12"

def test_when_3_return_123():
    result = print_num(3)
    assert result == "123"
