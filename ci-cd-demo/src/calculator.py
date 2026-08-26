"""シンプルな計算モジュール — CI/CDデモ用"""


def add(a: int, b: int) -> int:
    """足し算"""
    return a + b


def subtract(a: int, b: int) -> int:
    """引き算"""
    return a - b


def multiply(a: int, b: int) -> int:
    """掛け算"""
    return a * b


def divide(a: int, b: int) -> float:
    """割り算（ゼロ除算はエラー）"""
    if b == 0:
        raise ValueError("ゼロで割ることはできません")
    return a / b
