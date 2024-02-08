
# ФУНКЦІЯ caching_fibonacci
#     Створити порожній словник cache

#     ФУНКЦІЯ fibonacci(n)
#         Якщо n <= 0, повернути 0
#         Якщо n == 1, повернути 1
#         Якщо n у cache, повернути cache[n]

#         cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
#         Повернути cache[n]

#     Повернути функцію fibonacci
# КІНЕЦЬ ФУНКЦІЇ caching_fibonacci


def caching_fibonacci():
    cache = {}   # Створення словника для зберігання кешу
    def fibonacci(n):
        if n <=0:  
            return 0 
        elif n==1:    
            return 1   
        elif n in cache:   
            return cache[n] # Якщо число вже обраховувалось повернення його з кешу
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2) # Розрахунок числа якого немає в кеші 
            return cache[n]
    return fibonacci

fib = caching_fibonacci()
print(fib(5))
print(fib(8))
print(fib(10))