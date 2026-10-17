import math

print("=== ЗАВДАННЯ 1: Обчислення похибок функції багатьох змінних ===")
# Вхідні дані та їх похибки
a1 = 0.12456
b1 = 0.12078
c1 = 2.08
delta_a1 = 0.0005
delta_b1 = 0.00003
delta_c1 = 0.015

# Обчислення значення функції f
# f = (2 * a * ln(2a + c)) / (a - b)^(1/3)
f_val = (2 * a1 * math.log(2 * a1 + c1)) / ((a1 - b1) ** (1/3))
print(f"Номінальне значення функції f: {f_val:.6f}")

# Часткові похідні функції f по a, b, c
# df/da = 2 * [ (ln(2a+c) + 2a/(2a+c)) / (a-b)^(1/3) - (a*ln(2a+c)) / (3*(a-b)^(4/3)) ]
term_a_b_cbrt = (a1 - b1) ** (1/3)
term_a_b_43 = (a1 - b1) ** (4/3)
ln_term = math.log(2 * a1 + c1)

df_da = 2 * ( (ln_term + 2 * a1 / (2 * a1 + c1)) / term_a_b_cbrt - (a1 * ln_term) / (3 * term_a_b_43) )
df_db = 2 * a1 * ln_term / (3 * term_a_b_43)
df_dc = 2 * a1 / (term_a_b_cbrt * (2 * a1 + c1))

# Абсолютна похибка функції f
delta_f = abs(df_da) * delta_a1 + abs(df_db) * delta_b1 + abs(df_dc) * delta_c1
# Відносна похибка функції f
delta_rel_f = delta_f / abs(f_val)

print(f"Гранична абсолютна похибка (Delta f): {delta_f:.6f}")
print(f"Гранична відносна похибка (delta f): {delta_rel_f:.6f} (або {delta_rel_f * 100:.2f}%)")

# Визначення кількості правильних знаків
order = math.floor(math.log10(abs(f_val)))
correct_digits = 0
for k in range(1, 10):
    if delta_f <= 0.5 * 10**(order - k + 1):
        correct_digits = k
    else:
        break
print(f"Кількість правильних знаків: {correct_digits}\n")


print("=== ЗАВДАННЯ 2: Обернена задача теорії похибок ===")
# Вхідні дані
a2 = 0.2456
b2 = 0.01823
c2 = 0.0348
m = 5 # кількість правильних значущих цифр

# Обчислення значення функції g
# g = (a + b) / sqrt(a - b^2) - arcsin(a + c)
sqrt_term = math.sqrt(a2 - b2**2)
g_val = (a2 + b2) / sqrt_term - math.asin(a2 + c2)
print(f"Номінальне значення функції g: {g_val:.6f}")

# Визначення допустимої абсолютної похибки результату
# Знаходимо старший розряд числа
order_g = math.floor(math.log10(abs(g_val)))
# Для m правильних цифр похибка <= 0.5 * 10^(order_g - m + 1)
delta_g = 0.5 * 10**(order_g - m + 1)
print(f"Допустима абсолютна похибка результату (Delta g): {delta_g:.8f}")

# Часткові похідні функції g по a, b, c
# dg/da = 1/sqrt(a-b^2) - (a+b)/(2*(a-b^2)^(3/2)) - 1/sqrt(1-(a+c)^2)
dg_da = 1/sqrt_term - (a2 + b2) / (2 * sqrt_term**3) - 1/math.sqrt(1 - (a2 + c2)**2)
# dg/db = 1/sqrt(a-b^2) + b*(a+b)/(a-b^2)^(3/2)
dg_db = 1/sqrt_term + (b2 * (a2 + b2)) / (sqrt_term**3)
# dg/dc = -1/sqrt(1-(a+c)^2)
dg_dc = -1/math.sqrt(1 - (a2 + c2)**2)

# Коефіцієнт K (сума модулів часткових похідних - принцип рівних впливів)
K = abs(dg_da) + abs(dg_db) + abs(dg_dc)
print(f"Коефіцієнт K (сума модулів похідних): {K:.4f}")

# Знаходження допустимої похибки вхідних даних (Delta)
delta_input = delta_g / K
print(f"Допустима похибка задання вхідних даних (Delta a = Delta b = Delta c): {delta_input:.10f}")