# Функция сложения двух чисел
def add(a, b):
    return a + b

# Функция вычитания: из первого числа вычитается второе
def subtract(a, b):
    return a - b

# Функция умножения двух чисел
def multiply(a, b):
    return a * b

# Функция деления с обработкой ошибки деления на 0
def divide(a, b):
    if b == 0:
        raise ValueError("На ноль делить нельзя")  # выбрасываем исключение
    return a / b

# Функция вычисления остатка от деления с обработкой деления на 0
def modulo(a, b):
    if b == 0:
        raise ValueError("На ноль делить нельзя")  # выбрасываем исключение
    return a % b

# Функция проверки: является ли число чётным
def check(number):
    return number % 2 == 0
