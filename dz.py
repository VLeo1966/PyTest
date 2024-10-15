import pytest
from count_vowels import count_vowels  # предположим, что функция находится в файле count_vowels.py

def test_only_vowels():
    assert count_vowels("аеёийоуыэюя") ==11, "Должно вернуть 11 для 'аеёиоуыэюя'"
    assert count_vowels("АЕЁИЙОУЫЭЮЯ") == 11, "Должно вернуть 11 для 'АЕЁИОУЫЭЮЯ'"

def test_no_vowels():
    assert count_vowels("бвгджзклмнпрстхшщъь") == 0, "Должно вернуть 0 для строки без гласных"
    assert count_vowels("") == 0, "Должно вернуть 0 для пустой строки"

def test_mixed_string():
    assert count_vowels("Привет, как дела?") == 5, "Должно вернуть 5 для 'Привет, как дела?'"
    assert count_vowels("сКоЛьКо ГлАсНыХ") == 4, "Должно вернуть 4 для 'сКоЛьКо ГлАсНыХ'"

# Команда для запуска тестов: pytest
