#1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.
print('Задание №1')

list_number=[x for x in range(2,10)]
list_number2=[x for x in range(2,100)]
repetition={}

for number2 in list_number2:
    for number in list_number:
        if number2%number==0:
            if number in repetition:
                repetition[number]+=1
            else:
                repetition[number]=1

print(repetition)
print('-'*100)

#2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
# (помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.
print('Задание №2')

first_list = [8, 3, 15, 6, 4, 2]
second_list = []

for i, x in enumerate(first_list):
    if x%2==0:
        second_list.append(i)

print(f'Четные числа стоят на позициях {second_list}')
print('-'*100)

#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

print('Задание №3')

maximum_number=None

random_list = [random.randint(1,10) for _ in range(10)]
print(random_list)

for i, x in enumerate(random_list):
    if maximum_number is not None:
        if x>maximum_number:
            maximum_number=x
            maximum_index=i
        if x<minimum_number:
            minimum_number = x
            minimum_index = i
    else:
        maximum_number=x
        maximum_index = i
        minimum_number = x
        minimum_index=i

print(f'Индекс максимального числа {maximum_number} равен {maximum_index}')
print(f'Индекс максимального числа {minimum_number} равен {minimum_index}')

random_list[maximum_index]=minimum_number
random_list[minimum_index]=maximum_number

print(random_list)
print('-'*100)

#4. Определить, какое число в массиве встречается чаще всего.

print('Задание №4')

random_list = [random.randint(1,10) for _ in range(10)]
print(random_list)
dict={}
biggest_value=0

for number in random_list:
    for num in random_list:
        if number==num:
            if num in dict:
                dict[num]+=1
            else:
                dict[num]=1

for key, value in dict.items():
    if value>biggest_value:
        biggest_value=value
        biggest_key=key

print(biggest_key)
print('-'*100)

#5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
print('Задание №5')

random_list = [random.randint(-100,100) for _ in range(10)]
print(random_list)

i = 0
index = -1
while i < 10:
    if random_list[i] < 0 and index == -1:
        index = i
    elif random_list[i] < 0 and random_list[i] > random_list[index]:
        index = i
    i += 1

print(f'Максимальный отрицательный элемент равен {random_list[index]} и находится на позиции {index + 1}')
print('-'*100)

#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
print('Задание №6')

random_list = [random.randint(-100,100) for _ in range(10)]
print(random_list)

list=[x for x in random_list if min(random_list)<x<max(random_list)]
print(list)
print(sum(list))
print('-'*100)

#7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
print('Задание №7')

random_list = [random.randint(-100,100) for _ in range(10)]
print(random_list)
minimum_number=None
second_minimum_number=None

for i,number in enumerate(random_list):
    if minimum_number==None:
        minimum_number=number
        minimum_number_index = i
    else:
        if minimum_number>number:
            minimum_number=number
            minimum_number_index=i

del random_list[minimum_number_index]

for i,number in enumerate(random_list):
    if second_minimum_number==None:
        second_minimum_number=number
    else:
        if second_minimum_number>number:
            second_minimum_number=number

print(minimum_number, end=' ')
print(second_minimum_number)
print('-'*100)

#8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

print('Задание №8')

matrix=[[int(input('Введите цифры для матрицы: ')) for _ in range(4)] for _ in range(4)]

for line in matrix:
    line.append(sum(line))
    for item in line:
        print(f'{item:>4}', end=' ')
    print()

print('-'*100)
