#: task1
f1 = 12
f2 = 3
f3 = 8

a = f1 + f2
b = f1 - f2 - f3
c = f2 * f3 - f1
print(a, b, c)

name = input("please, enter your name: ")
date_of_birth = input("please, enter your date of birth: ")
print("Hi,", name, ". Your was born at ", date_of_birth, ".")

#: task2
s = int(input("please, enter duration of the race: "))
b = 3600
c = 60

h = s // b
m = s % b // c
s = s % b % c
print("The race lasted ", f'{h:02}h:{m:02}m:{s:02}s')

#: task3
n = int(input("please, enter number: "))
n1 = int(f'{n}{n}')
n2 = int(f'{n}{n}{n}')
summary = n + n1 + n2
print(summary)

#: task4
input_number = int(input("введите целое положительное число: "))
max_digit = 0
number2 = input_number
while number2 > 0:
    digit = number2 % 10
    if digit > max_digit:
        max_digit = digit
    number2 = number2 // 10

print(f'в числе {n} наибольшая цифра {max_digit}')

#: task5
_n_ = float(input('введите годовую выручку: '))
k = float(input('введите годовой расход: '))
delta = _n_ - k
if _n_ < k:
    print('дефицит составил ', delta, 'рублей')
elif _n_ == k:
    print('в этом году предприятие сработало безубыточно')
else:
    staff = int(input('введите количество сотрудников: '))
    rent = _n_ / k
    rent_personal = delta / staff
    print('профицит составляет ', delta, 'рублей')
    print('рентабельность составляет ', f'{rent:.2}', '%')
    print('прибыть в расчете на одного сотрудника - ', rent_personal, 'рублей')

#: task6
dist_1 = float(input('введите начальную дистанцию: '))
dist_2 = float(input('введите желаемую дистанцию: '))
days = 1
while dist_2 > dist_1:
    days += 1
    dist_1 = dist_1 + dist_1 * 0.1
else:
    print('вы достигнете желаемой дистации на', days, 'дней')
