import pytest

from algorithm.ten_puzzle.poland import calc_poland


def test_calc_poland1():
    """正常動作"""
    exp = "612+*8-"
    assert calc_poland(exp) == 10


def test_calc_poland2():
    """数字と演算子以外の異常系動作"""
    exp = "612+a*8-"
    with pytest.raises(Exception) as e:
        calc_poland(exp)
    assert str(e.value) == "数字と演算子以外は入力しないでください"
