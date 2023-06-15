""" №1.1[1]. За день шина проезжает n километров.
Сколько дней нужно, чтобы проехать маршрут длиной m километров?
Реализуйте пользовательский ввод данных и вывод внятного результата. Используйте .format() или f-строки
Примеры/Тесты:
n = 700, m = 750 -> Чтобы проехать 750км машине потребуется 2дн
n = 700, m = 600 -> Чтобы проехать 600км машине потребуется 1дн
n = 700, m = 1400 -> Чтобы проехать 1400км машине потребуется 2дн
Усложнение[*]. Использовать тернарный оператор """

count = int(input('За день шина проезжает n километров:'))
distance = int(input('Маршрут длиной m километров:'))
# count = 700
# distance = 600
# days = -distance//count
# print(-days)

if distance % count != 0:
    days = distance//count+1
else:
    days = distance//count

# placeholder
print(f'Чтобы проехать {distance} км машине потребуется {days} дн')

days2 = distance//count+1 if distance % count != 0 else distance//count

print(f'Чтобы проехать {distance} км машине потребуется {days2} дн')

print(
    f'Чтобы проехать {distance} км машине потребуется {distance//count+1 if distance%count != 0 else distance//count} дн')
