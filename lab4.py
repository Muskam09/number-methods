import math

# Функція 1 та її похідні
def f1(x): return 3 * x**4 + 8 * x**3 + 6 * x**2 - 11
def df1(x): return 12 * x**3 + 24 * x**2 + 12 * x
def d2f1(x): return 36 * x**2 + 48 * x + 12

# Функція 2 та її похідні
def f2(x): return 5**x + math.exp(x) - 3
def df2(x): return 5**x * math.log(5) + math.exp(x)
def d2f2(x): return 5**x * (math.log(5))**2 + math.exp(x)

# Метод Ньютона (дотичних)
def newton_method(f, df, d2f, a, b, eps=1e-7):
    # Крок 1: Вибір початкової точки x0
    if f(a) * d2f(a) > 0:
        xn = a
    else:
        xn = b
        
    iterations = 0
    # Крок 2: Ітераційний процес
    while True:
        iterations += 1
        df_xn = df(xn)
        
        if abs(df_xn) < 1e-15:
            break
            
        # Крок 3: Формула Ньютона
        x_next = xn - f(xn) / df_xn
        
        # Крок 4: Перевірка зупинки
        if abs(x_next - xn) < eps:
            return x_next, iterations
            
        xn = x_next
        
    return xn, iterations

# Виконання та виведення
print("--- МЕТОД НЬЮТОНА (ε = 10^-7) ---")
root1, iter1 = newton_method(f1, df1, d2f1, 0.0, 1.0)
print(f"Рівняння 1: x ≈ {root1:.7f} | Ітерацій: {iter1}")

root2, iter2 = newton_method(f2, df2, d2f2, 0.0, 1.0)
print(f"Рівняння 2: x ≈ {root2:.7f} | Ітерацій: {iter2}")