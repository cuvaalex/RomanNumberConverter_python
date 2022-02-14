import unittest

import pytest

from elseif.elseif import isWeird


@pytest.mark.parametrize("x", [2, 4])
def test_return_isNotWeird_if_n_isEven_and_into_range(x):
    result = isWeird(x)

    assert "Not Weird" == result

@pytest.mark.parametrize("x", [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23])
def test_return_isWeird_if_isOdd(x):
    result = isWeird(x)

    assert "Weird" == result
@pytest.mark.parametrize("x", [6, 8, 20])
def test_return_isWeird_if_x_between_6_and_20(x):
    result = isWeird(x)

    assert "Weird" == result


