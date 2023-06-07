#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""例題プログラム
"""

__author__ = "Taku Ikegami"
__version__ = "1.0.1"
__date__ = "2023/06/07(Created: 2023/06/07)"

from algorithm import example


def test_main():
    """例題プログラムのテスト"""
    assert example.main() == "HelloWorld"
