"""
Проведите тест гипотезы. Утверждается, что шарики для подшипников, изготовленные автоматическим станком,
имеют средний диаметр 17 мм.
Используя односторонний критерий с α=0,05, проверить эту гипотезу, если в выборке из n=100 шариков средний диаметр
оказался равным 17.5 мм, а дисперсия известна и равна 4 кв. мм.
"""

import scipy.stats as stats

# Исходные данные
sample_mean = 17.5  # среднее значение выборки
population_mean = 17  # предполагаемое среднее значение генеральной совокупности
population_variance = 4  # дисперсия генеральной совокупности
n = 100  # размер выборки
alpha = 0.05  # уровень значимости

# Расчет стандартного отклонения генеральной совокупности
population_std_dev = population_variance ** 0.5

# Расчет Z-статистики
Z = (sample_mean - population_mean) / (population_std_dev / (n ** 0.5))

# Определение критического значения Z для альфа
Z_critical = stats.norm.ppf(1 - alpha)

# Вывод результатов
print(f"Z-статистика: {Z}")
print(f"Z-критическое (для одностороннего теста): {Z_critical}")

# Принятие или отклонение нулевой гипотезы
if Z > Z_critical:
    print("Отклоняем нулевую гипотезу, средний диаметр шариков статистически значимо больше 17 мм.")
else:
    print("Нет оснований отклонять нулевую гипотезу.")
