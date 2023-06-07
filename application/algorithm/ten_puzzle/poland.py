#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""テンパズル 〜力任せ探索
"""

from enum import Enum


class Operator(Enum):
    """演算子

    Attributes:
        ADD: 加算演算子
        SUB: 減算演算子
        MUL: 乗算演算子
        DIV: 除算演算子
    """

    ADD = ("+", lambda x, y: x + y)
    SUB = ("-", lambda x, y: x - y)
    MUL = ("*", lambda x, y: x * y)
    DIV = ("/", lambda x, y: x / y)

    @classmethod
    def get_operator_method(cls, value):
        """演算子に対応するメソッドを返却

        Args:
            value (str): 演算子

        Returns:
            演算子に対応するメソッド
        """
        for operator in cls:
            if operator.value[0] == value:
                return operator.value[1]
        return None


def calc_poland(exp: str):
    """逆ポーランド記法

    Args:
        exp (str): 逆ポーランド記法の数式

    Returns:
        int: 計算結果
    """
    results = []

    for e in exp:
        if "0" <= e <= "9":
            results.append(int(e))
        else:
            operator_method = Operator.get_operator_method(e)
            if operator_method is None:
                raise Exception("数字と演算子以外は入力しないでください")
            num1 = results.pop()
            num2 = results.pop()
            results.append(operator_method(num2, num1))
    return results.pop()
