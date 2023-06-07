#!/usr/bin/env python3
# -*- coding: utf_8 -*-
from algorithm.komachi_calculation.arithmetic_processing import (
    calc_add_sub,
    calc_empty,
    calc_mul_div,
)


def test_calc_empty1():
    """空白処理の動作確認"""
    signs = [1, 0, 0, 3, 4, 2, 2, 0]
    expected = ([1, 234, 5, 6, 7, 89], [1, 3, 4, 2, 2])
    assert calc_empty(signs) == expected


def test_calc_mul_div1():
    """掛け算、割り算の部分の動作確認"""
    vals = [1, 234, 5, 6, 7, 89]
    signs = [1, 3, 4, 2, 2]
    expected = (
        [1, 195, 7, 89],
        [1, 2, 2],
    )
    assert calc_mul_div(vals, signs) == expected


def test_calc_add_sub():
    """足し算、引き算の部分の動作確認"""
    vals = [1, 195, 7, 89]
    signs = [1, 2, 2]
    expected = 100
    assert calc_add_sub(vals, signs) == expected
