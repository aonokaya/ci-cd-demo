"""text_utils.py のテスト"""

from src.text_utils import count_words, is_palindrome, reverse_string

# ========== reverse_string のテスト ==========

def test_reverse_normal():
    """通常の文字列を反転"""
    assert reverse_string("hello") == "olleh"


def test_reverse_empty():
    """空文字列の反転"""
    assert reverse_string("") == ""


def test_reverse_japanese():
    """日本語文字列の反転"""
    assert reverse_string("テスト") == "トステ"


# ========== count_words のテスト ==========

def test_count_words_normal():
    """通常の文章"""
    assert count_words("hello world foo") == 3


def test_count_words_single():
    """単語ひとつ"""
    assert count_words("hello") == 1


def test_count_words_empty():
    """空文字列"""
    assert count_words("") == 0


def test_count_words_whitespace_only():
    """スペースだけ"""
    assert count_words("   ") == 0


# ========== is_palindrome のテスト ==========

def test_palindrome_true():
    """回文"""
    assert is_palindrome("racecar") is True


def test_palindrome_false():
    """回文ではない"""
    assert is_palindrome("hello") is False


def test_palindrome_with_spaces():
    """スペース込みの回文"""
    assert is_palindrome("nurses run") is True


def test_palindrome_case_insensitive():
    """大文字小文字を無視した回文"""
    assert is_palindrome("Madam") is True
