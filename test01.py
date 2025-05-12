import unittest  # библиотека для модульного тестирования
from main01 import add, subtract, multiply, divide, modulo, check  # импорт функций из main02.py

# Тесты для математических операций
class TestMath(unittest.TestCase):

    # Тесты для функции сложения
    def test_add(self):
        self.assertEqual(add(2, 5), 7)  # ожидаем правильный результат
        self.assertNotEqual(add(3, 7), 9)  # проверка на ошибочный результат

    # Тесты для функции вычитания
    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)
        self.assertNotEqual(subtract(4, 2), 1)

    # Тесты для функции умножения
    def test_multiply(self):
        self.assertNotEqual(multiply(2, 5), 12)
        self.assertEqual(multiply(3, 6), 18)

    # Тесты для функции деления
    def test_divide(self):
        self.assertNotEqual(divide(4, 2), 3)
        self.assertEqual(divide(20, 5), 4)

    # Проверка деления на 0: ожидается исключение ValueError
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(6, 0)

    # Тесты для функции вычисления остатка
    def test_modulo_success(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(20, 5), 0)
        self.assertEqual(modulo(7, 2), 1)

    # Проверка остатка от деления на 0: должно возникнуть исключение
    def test_modulo_by_zero(self):
        with self.assertRaises(ValueError):
            modulo(5, 0)

# Тесты для функции проверки чётности
class TestCheck(unittest.TestCase):

    def test_check(self):
        self.assertTrue(check(2))     # чётные числа
        self.assertTrue(check(6))
        self.assertTrue(check(220))
        self.assertFalse(check(1))    # нечётные числа
        self.assertFalse(check(3))
        self.assertFalse(check(57))

# Запуск всех тестов при прямом запуске файла
if __name__ == '__main__':
    unittest.main()
