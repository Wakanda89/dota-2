total_distance = 0  # Инициализация общей дистанции

# Цикл по первым 7 дням
for day in range(7):
    total_distance += 10 * (1.1 ** day)  # Расчет пробега по формуле

# Вывод результата
print(f'Суммарный путь за первые 7 дней тренировок: {total_distance:.2f} км')
