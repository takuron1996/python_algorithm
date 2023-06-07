#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""小町算（演算処理の実装）

1 ▫️ 2 ▫️ 3 ▫️ 4 ▫️ 5 ▫️ 6 ▫️ 7 ▫️ 8 ▫️ 9 = 100

▫️ には演算子が入る
    ・空白
    ・+
    ・-
    ・*
    ・/

Step1: 最初に、空白を処理（数字を連結）
Step2: 掛け算、割り算の部分を処理
Step3: 足し算、引き算の部分を処理
"""

from enum import IntEnum


class Operator(IntEnum):
    """演算子

    Attributes:
        EMPTY: 空白
        ADD: 加算演算子
        SUB: 減算演算子
        MUL: 乗算演算子
        DIV: 除算演算子
    """

    EMPTY = 0
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4

    @classmethod
    def get_operator_method(cls, value: int):
        """演算子に対応した関数を返却

        Args:
            value (int): 演算子の数値

        Returns:
            演算子に対応した関数
        """
        operator = {
            cls.ADD: lambda x, y: x + y,
            cls.SUB: lambda x, y: x - y,
            cls.MUL: lambda x, y: x * y,
            cls.DIV: lambda x, y: x // y,
        }
        return operator.get(value)


def calc_empty(signs: list[int]):
    """空白部分の計算処理

    Args:
        signs (list[int]): 演算子を数字で表現したリスト

    Returns:
        tuple(list[int], list[int]): (数値, 演算子)
    """
    new_vals = []
    new_signs = []

    # 途中経過の値（小町算の最初の値は1）
    val = 1

    for i in range(len(signs)):
        next_val = i + 2

        if signs[i] == Operator.EMPTY:
            val = val * 10 + next_val
        else:
            new_vals.append(val)
            new_signs.append(signs[i])
            val = next_val
    new_vals.append(val)
    return (new_vals, new_signs)


def calc_mul_div(vals: list[int], signs: list[int]):
    """掛け算、割り算の部分の計算処理

    Args:
        vals (list[int]): 計算する数値
        signs (list[int]): 演算子を数字で表現したリスト

    Returns:
        tuple(list[int], list[int]): (数値, 演算子)
    """
    new_vals = []
    new_signs = []

    # 途中経過の値
    val = vals[0]

    for i in range(len(signs)):
        next_val = vals[i + 1]

        if signs[i] in (Operator.MUL, Operator.DIV):
            operator_method = Operator.get_operator_method(signs[i])
            val = operator_method(val, next_val)
        else:
            new_vals.append(val)
            new_signs.append(signs[i])
            val = next_val
    new_vals.append(val)
    return (new_vals, new_signs)


def calc_add_sub(vals: list[int], signs: list[int]):
    """足し算、引き算の部分の計算処理

    Args:
        vals (list[int]): 計算する数値
        signs (list[int]): 演算子を数字で表現したリスト

    Returns:
        tuple(list[int], list[int]): (数値, 演算子)
    """
    result = vals[0]

    for i in range(len(signs)):
        next_val = vals[i + 1]
        operator_method = Operator.get_operator_method(signs[i])
        result = operator_method(result, next_val)
    return result
