"""calculator.py のテスト"""

import pytest
from src.calculator import add, subtract, multiply, divide


# ========== add のテスト ==========

def test_add_positive_numbers():
    """正の数同士の足し算"""
    assert add(2, 3) == 5


def test_add_negative_numbers():
    """負の数同士の足し算"""
    assert add(-1, -1) == -2


def test_add_zero():
    """ゼロを足す"""
    assert add(5, 0) == 5


# ========== subtract のテスト ==========

def test_subtract_basic():
    """基本的な引き算"""
    assert subtract(10, 3) == 7


def test_subtract_negative_result():
    """結果がマイナスになる引き算"""
    assert subtract(3, 10) == -7


# ========== multiply のテスト ==========

def test_multiply_basic():
    """基本的な掛け算"""
    assert multiply(4, 5) == 20


def test_multiply_by_zero():
    """ゼロを掛ける"""
    assert multiply(100, 0) == 0


# ========== divide のテスト ==========

def test_divide_basic():
    """基本的な割り算"""
    assert divide(10, 2) == 5.0


def test_divide_with_decimal():
    """割り切れない割り算"""
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    """ゼロ除算はエラーになるべき"""
    with pytest.raises(ValueError, match="ゼロで割ることはできません"):
        divide(10, 0)
