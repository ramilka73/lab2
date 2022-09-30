import numpy as np
from numpy import linalg

m = int(input('Введите размерность квадратной матрицы больше 1 и меньше 31:'))
while (m < 1) or (m > 31):
    m = int(input("Вы ввели неверное число. "
                  "\nВведите количество строк (столбцов) квадратной матрицы больше 1 и меньше 31:"))
a = np.random.randint(5, size=(m, m))
r = np.linalg.matrix_rank(a)
print("Матрица:\n", a)
print("Ранг матрицы:", r)
t = int(input('Введите количество знаков после запятой в результате вычисления:'))
t = 0.1 ** t
n = 1
fact = 1
summa = 0
fg = 0
out = 1
while abs(out) > t:
    fg += summa
    summa += (np.linalg.det(linalg.matrix_power(a, 2 * n + 1))) / fact
    n += 1
    fact = fact * (2*n + 1) * (2*n + 2)
    out = abs(fg-summa)
    fg = 0
    print(n+1, ':', summa, ' ', out)
print('Сумма знакопеременного ряда:', summa)
