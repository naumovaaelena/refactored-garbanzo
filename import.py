import matplotlib.pyplot as plt

# Рекурсивная функция для вычисления чисел Фибоначчи
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Функция для динамического вычисления чисел Фибоначчи (с мемоизацией)
def fibonacci_dynamic(n):
    memo = {0: 0, 1: 1}
    
    def fib(n):
        if n not in memo:
            memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
    
    return fib(n)

# Вычисление первых N чисел Фибоначчи
def generate_fibonacci_sequence(n, method='recursive'):
    sequence = []
    for i in range(n):
        if method == 'recursive':
            sequence.append(fibonacci_recursive(i))
        elif method == 'dynamic':
            sequence.append(fibonacci_dynamic(i))
    return sequence