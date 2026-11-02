import math

# Функція 1: 3x^4 + 8x^3 + 6x^2 - 11 = 0
def f1(x):
    return 3 * x**4 + 8 * x**3 + 6 * x**2 - 11

# Функція 2: 5^x + e^x - 3 = 0
def f2(x):
    return 5**x + math.exp(x) - 3

# Метод дихотомії (половинного ділення)
def bisection_method(f, a, b, eps=1e-7):
    # Крок 1. Перевірка наявності кореня
    if f(a) * f(b) > 0:
        return None, 0
    
    iterations = 0
    # Крок 2. Цикл працює, поки довжина відрізка більша за точність
    while abs(b - a) > eps:
        iterations += 1
        x_mid = (a + b) / 2.0 
        
        # Крок 3. Визначаємо нові межі
        if f(a) * f(x_mid) < 0:
            b = x_mid
        else:
            a = x_mid
            
    # Крок 4. Повертаємо корінь
    return (a + b) / 2.0, iterations

# Виконання та виведення
print("--- МЕТОД ДИХОТОМІЇ (ε = 10^-7) ---")
root1, iter1 = bisection_method(f1, 0.0, 1.0)
print(f"Рівняння 1: x ≈ {root1:.7f} | Ітерацій: {iter1}")

root2, iter2 = bisection_method(f2, 0.0, 1.0)
print(f"Рівняння 2: x ≈ {root2:.7f} | Ітерацій: {iter2}")