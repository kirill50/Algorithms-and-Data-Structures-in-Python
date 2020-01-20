#1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для
# каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import OrderedDict, Counter

data=OrderedDict()
N=int(input('Введите кол-во предприятий: '))

for i in range(N):
    name=input('Введите имя предприятия: ')
    for i1 in range(1,5):
        if name not in data:
            data[name] = int(input(f'Введите прибыль за {i1} квартал:'))
        else:
            data[name]=int(input(f'Введите прибыль за {i1} квартал:'))+data[name]
print(data)

average_income=sum(data.values())/N
print(f'Средняя прибыль по всем предприятиям за год равна {average_income}.')

lst=Counter(data)
n=int(input("Какое кол-во предприятий распечать, которые наиболее отклоняются от среднего: "))
bigger=lst.most_common(n)[0][0]
less=lst.most_common()[:-n-1:-1][0][0]
print(f'В меньшую сторону отличаются предприятия {less},а в большую {bigger}.')

#2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

import re
from collections import deque

first_number=input("Вводим 1-ое шестнадцатеричное число: ").upper()
second_number=input("Вводим 2-ое шестнадцатеричное число: ").upper()

common_first_number=0
common_second_number=0
n_1=0
n_2=0

Meanings={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

if re.search(r'[^A-F0-9]',first_number):
     print("Введен какой то бред. Повторить!")
elif re.search(r'[^A-F0-9]',second_number):
    print("Введен какой то бред. Повторить!")
else:
     first_list=list(first_number)
     second_list=list(second_number)

     for digit in reversed(first_list):
         common_digit=Meanings[digit]*16**n_1
         n_1+=1
         common_first_number=common_digit+common_first_number

     for digit in reversed(second_list):
         common_digit=Meanings[digit]*16**n_2
         n_2+=1
         common_second_number=common_digit+common_second_number

     multiplication=common_first_number*common_second_number
     sum=common_first_number+common_second_number

     print(multiplication, sum)

     multi_16=deque()
     sum_16=deque()

    #произведение
     while True:
         if multiplication>16:
             number=[keys for keys, vals in Meanings.items() if vals == multiplication % 16][0]
             multi_16.appendleft(number)
             multiplication=multiplication//16
         elif multiplication!=0:
             number = [keys for keys, vals in Meanings.items() if vals == multiplication % 16][0]
             multi_16.appendleft(number)
             multiplication=0
         else:
             break

    #Сумма
     while True:
         if sum > 16:
             number = [keys for keys, vals in Meanings.items() if vals == sum % 16][0]
             sum_16.appendleft(number)
             sum = sum // 16
         elif sum != 0:
             number = [keys for keys, vals in Meanings.items() if vals == sum % 16][0]
             sum_16.appendleft(number)
             sum = 0
         else:
             break

     print(f'Произведение равно {multi_16}')
     print(f'Произведение равно {sum_16}')