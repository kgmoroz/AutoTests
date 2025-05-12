# main.py

def count_vowels(s):
    # Определяем все русские гласные (строчные и заглавные)
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"

    # Считаем количество символов в строке s, которые входят в набор гласных
    return sum(1 for char in s if char in vowels)
