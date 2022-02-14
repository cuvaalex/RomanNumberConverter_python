import pytest

from kata.roman_number_converter import RomanNumber

@pytest.mark.parametrize("number, expected",
                         [
                             (1, "I"),
                             (2, "II"),
                             (3, "III"),
                             (5, "V"),
                             (6, "VI"),
                             (7, "VII"),
                             (10, "X"),
                             (11, "XI"),
                             (20, "XX"),
                             (30, "XXX"),
                             (41, "XLI"),
                             (50, "L"),
                             (51, "LI"),
                             (54, "LIV"),
                             (60, "LX"),
                             (99, "XCIX"),
                             (100, "C"),
                             (111, "CXI"),
                             (253, "CCLIII")
                         ])
def test_return_xI_when_n(number, expected):
    romanNumber = RomanNumber()
    assert expected == romanNumber.parse(number)

def test_return_IV_when_4():
    romanNumber = RomanNumber()
    assert "IV" == romanNumber.parse(4)

def test_return_IX_when_9():
    romanNumber = RomanNumber()
    assert "IX" == romanNumber.parse(9)

def test_return_XIV_when_14():
    romanNumber = RomanNumber()
    assert "XIV" == romanNumber.parse(14)

def test_return_XIX_when_19():
    romanNumber = RomanNumber()
    assert "XIX" == romanNumber.parse(19)

def test_return_XL_when_40():
    romanNumber = RomanNumber()
    assert "XL" == romanNumber.parse(40)

def test_return_XC_when_90():
    romanNumber = RomanNumber()
    assert "XC" == romanNumber.parse(90)
