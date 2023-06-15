# №1.2[3]. В некоторой школе решили набрать три новых математических класса
# и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся
#  в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Примеры/Тесты:
# 20 21 22(ввод чисел НЕ в одну строку) -> Общее кол-во парт будет 32
# 21 21 21(ввод чисел НЕ в одну строку) -> Общее кол-во парт будет 33

""" class1 = int(input('Enter number of students in 1st class: '))
class2 = int(input('Enter number of students in 2st class: '))
class3 = int(input('Enter number of students in 3st class: '))

countDesk1 = class1 // 2 if class1 % 2 == 0 else class1 // 2+1
countDesk2 = class2 // 2 if class2 % 2 == 0 else class2 // 2+1
countDesk3 = class3 // 2 if class3 % 2 == 0 else class3 // 2+1

print (f'Total amount of desks {countDesk1 + countDesk2 + countDesk3}') """

count_desk = 0
for class_number in range(3):
    studets = int(input(f'Enter number of students in {class_number+1}st class: '))
    count_desk += studets // 2 if studets % 2 == 0 else studets // 2+1
print (f'Total amount of desks {count_desk}')