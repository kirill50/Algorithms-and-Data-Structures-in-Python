#1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания
# первых трех уроков.
#Примечание. Идеальным решением будет:
#a. выбрать хорошую задачу, которую имеет смысл оценивать,
#b. написать 3 варианта кода (один у вас уже есть),
#c. проанализировать 3 варианта и выбрать оптимальный,
#d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
#e. написать общий вывод: какой из трёх вариантов лучше и почему.

#Общий вывод: самый удобный вариант №1(обычный цикл), потому что он самый быстрый по скорости
# и не имеет тех ограничений, которые имеет рекурсия (Вариант №2), а вариант с сохранениеми в словарь
# работает чуть дольше.

#Task_9: Вводим числа, выбираем наибольшее по сумме цифр.
import random
import cProfile
print('Вариант_1:')

def biggest_loop(n):
    biggest_sum=0

    while True:
        for i in range(n):

            #number=int(input("Введите натуральное число: "))
            number = random.randint(1, 1000000)
            num=number
            total_sum=0
            while number>0:
                digit = number % 10
                total_sum=total_sum+digit
                number //= 10

            if total_sum>biggest_sum:
                biggest_sum=total_sum
                biggest_num=num

            if (i+1)==n:
                break

        return biggest_sum, biggest_num

x=biggest_loop(10)
print(f'Наибольшее число по сумме цифр является {x[1]}. Сумма цифр {x[0]}.')

#timeit: Зависимость линейная
#biggest_loop(10) - best of 5: 21.3 usec per loop
#biggest_loop(20) - best of 5: 40.8 usec per loop
#biggest_loop(100) - best of 5: 203 usec per loop
#biggest_loop(200) - best of 5: 408 usec per loop

#cProfile.run('biggest_loop(10)') - lesson_4.py:15(biggest_loop) - 1
#cProfile.run('biggest_loop(20)') - lesson_4.py:15(biggest_loop) - 1
...

print('Вариант_2:')
def biggest_rec(n,biggest_sum=0, biggest_num=0):
    for i in reversed(range(n)):
        #number = int(input("Введите натуральное число: "))
        number=random.randint(1,1000000)
        saved_number = number
        total_sum = 0

        while number > 0:
            digit = number % 10
            total_sum = total_sum + digit
            number //= 10

        if total_sum > biggest_sum:
            biggest_sum = total_sum
            biggest_num = saved_number

        if i==0:
            return biggest_sum, biggest_num

        biggest_sum, biggest_num = biggest_rec(n-1,biggest_sum, biggest_num)       #Важно запомнить !
        return biggest_sum, biggest_num

x=biggest_rec(10)

print(f'Наибольшее число по сумме цифр является {x[1]}. Сумма цифр {x[0]}.')

#timeit:  Зависимость линейная
#biggest_rec(10) - best of 5: 27.6 usec per loop
#biggest_rec(20) - best of 5: 55.4 usec per loop
#biggest_rec(100) - best of 5: 280 usec per loop
#biggest_rec(200) - best of 5: 561 usec per loop
# На тысячи переполнение рекурсии

#cProfile.run('biggest_rec(10)') - lesson_4.py:5(biggest_rec) - 10
#cProfile.run('biggest_rec(20)') - lesson_4.py:5(biggest_rec) - 20
#cProfile.run('biggest_rec(100)') - lesson_4.py:5(biggest_rec) - 100
#cProfile.run('biggest_rec(200)') - lesson_4.py:5(biggest_rec) - 200

print('Вариант_3:')

def biggest_dict(n,biggest_sum=0, biggest_num=0):
    numbers = []
    sums = []
    for i in reversed(range(n)):
        # number = int(input("Введите натуральное число: "))
        number=random.randint(1,1000000)
        numbers.append(number)
        total_sum = 0

        while number > 0:
            digit = number % 10
            total_sum = total_sum + digit
            number //= 10
        sums.append(total_sum)

        if i == 0:
            l_max=[]
            d = dict(zip(numbers, sums))
            for key, val in d.items():
                if not (l_max):
                    l_max.append((key, val))
                elif l_max[0][1] < val:
                    l_max = [(key, val)]
                elif l_max[0][1] == val:
                    l_max.append((key, val))
            return l_max

x=biggest_dict(10000)

print(f'Наибольшее число по сумме цифр является {[i[0] for i in x]}. Сумма цифр {x[0][1]}.')

#timeit: Зависимость линейная
#biggest_dict(10) - best of 5: 24.7 usec per loop
#biggest_dict(20) - best of 5: 48.4 usec per loop
#biggest_dict(100) - best of 5: 240 usec per loop
#biggest_dict(200) - best of 5: 476 usec per loop

#cProfile.run('biggest_dict(10)') - lesson_4.py:6(biggest_dict) - 1
#                                 - {method 'append' of 'list' objects} - 22
#cProfile.run('biggest_dict(20)') - lesson_4.py:6(biggest_dict) - 1
# #                                 - {method 'append' of 'list' objects} - 41
#cProfile.run('biggest_dict(100)') - lesson_4.py:6(biggest_dict) - 1
#                                 - {method 'append' of 'list' objects} - 203
#cProfile.run('biggest_dict(200)') - lesson_4.py:6(biggest_dict) - 1
#                                 - {method 'append' of 'list' objects} - 403

#2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого
# числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать
# скорость и сложность алгоритмов.
#Первый — с помощью алгоритма «Решето Эратосфена».
#Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#Второй — без использования «Решета Эратосфена».
#Примечание. Вспомните классический способ проверки числа на простоту.

#Общий вывод: Второй вариант намного лучше, потому что там простые числа ищутся до определенного индекса,
# который мы задали. Засчет этого получается гораздо меньше итераций.

import math

print('Задание №2')
print('Вариант №1')


def eratosfen(y):
    n = 10000
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):

        if sieve[i] != 0:
            j = i * 2

            while j < n:
                sieve[j] = 0
                j += i

    result = [i for i in sieve if i != 0]
    # index=int(input('Введите индекс простого числа для вывода:'))
    index = y
    print(result[index])

eratosfen(5)

print()
#timeit:
#1000 loops, best of 5: 3.17 msec per loop

#cProfile.run('eratosfen(5)') - lesson_4.py:8(eratosfen) - 1

print('Вариант №2')

def isPrime(n):
  for j in range(3, int(n**0.5)+1):
    if n%j==0:
      return 0
  return 1

def search(n):
    primes = [2]
    i = 3
    last_simple=2
    while len(primes)<n:
        if isPrime(i) == 1:
            primes.append(i)
            last_simple=i
        i+=2
    return last_simple

print(search(5+1))

#timeit:
#1000 loops, best of 5: 3.98 usec per loop

#cProfile.run('search(5+1)') - lesson_4.py:8(search) - 1
#                                            isPrime - 6