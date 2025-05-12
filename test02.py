# test02.py

import pytest  # импортируем pytest
from main02 import count_vowels  # импортируем нашу функцию из main02.py


# Тест 1: строка содержит только гласные (строчные и заглавные)
def test_all_vowels():
    assert count_vowels("аеёиоуыэюяАЕЁИОУЫЭЮЯ") == 20  # Всего 20 гласных


# Тест 2: строка не содержит гласных
def test_no_vowels():
    assert count_vowels("бцжнйх") == 0


# Тест 3: строка содержит и гласные, и другие символы
def test_mixed_string():
    assert count_vowels("Привет, как дела?") == 5  # и, е, а, е, а


# Параметризованный тест — несколько вариантов на вход
@pytest.mark.parametrize("input_str, expected", [
    ("", 0),                # Пустая строка — 0 гласных
    ("москва", 2),          # о, а
    ("СПб", 0),             # Нет гласных
    ("ДоСвИдАнИя", 5),      # о, и, а, и, я
    ("12345", 0),           # Только цифры — 0 гласных
])
def test_parametrized(input_str, expected):
    assert count_vowels(input_str) == expected
