"""テキスト処理ユーティリティ — CI/CDデモ用"""


def reverse_string(text: str) -> str:
    """文字列を反転する"""
    return text[::-1]


def count_words(text: str) -> int:
    """単語数をカウントする（空白区切り）"""
    if not text.strip():
        return 0
    return len(text.split())


def is_palindrome(text: str) -> bool:
    """回文かどうか判定する（大文字小文字・スペース無視）"""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
