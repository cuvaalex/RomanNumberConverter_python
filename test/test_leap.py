import pytest
from leapyear.leap_year import is_leap

@pytest.mark.parametrize("year", [2000, 2400])
def test_is_leap_if_2000_divided_by_4(year):
    result = is_leap(year)
    assert result

def test_is_not_leap_if_1999_not_divided_by_4():
    result = is_leap(1999)
    assert result == False

def test_leap_if_2000_divided_by_400():
    result = is_leap(2000)
    assert result == True
