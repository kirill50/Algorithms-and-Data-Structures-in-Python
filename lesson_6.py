#1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
# программах в рамках первых трех уроков. Проанализировать результат и определить
# программы с наиболее эффективным использованием памяти.

#Вариант_1: Общая сумма занимаего места = 392
#Вариант_2: Общая сумма занимаего места = 22344
#Вариант_3: Общая сумма занимаего места = 3160

#Вывод: с позиции использования памяти вариант номер 1 самый эффективный. Потому что
# информация хранится здесь везде в качетстве цифр и занимает минимальное кол-во памяти.
#На 2 месте вариант номер 3 со словарем, его плюс это то что там могут хранится одновременно
#несколько максимальных чисел и выводятся тоже несколько. В варианте номер три боюсь, что то
# не правильно срабатывает в подсчете памяти засчет рекурсии. Буду благодарен, если кто подскажет.

import random, sys, re

print(f'Python 3.7.3, ОС: MacOS Mojave 10.14.6 ')
print()

n=random.randint(10,100) #добавил, чтобы число выбиралось случайным образом для всех 3 х вариантов одинаковое

def show_size(x,result=[]):
    #print('\t'*level, f'type={x.__class__},size={sys.getsizeof(x)}, object={x}')
    a=f'type={x.__class__}//size={sys.getsizeof(x)}//object={x}'
    result.append(a)

    return result

print('Вариант_1:')

def biggest_loop(n):
    biggest_sum=0

    while True:
        for i in range(n):
            #number=int(input("Введите натуральное число: "))
            #number = random.randint(1, 1000000)
            number=50-i  #чтобы сравнение было по равным числам
            num=number
            total_sum=0

            inside=[]
            inside.extend(show_size(num))       #память переменной

            while number>0:
                digit = number % 10
                total_sum=total_sum+digit
                number //= 10

            if total_sum>biggest_sum:
                biggest_sum=total_sum
                biggest_num=num

                inside.extend(show_size(biggest_sum))          #память переменной
                inside.extend(show_size(biggest_num))          #память переменной

            if (i+1)==n:
                break

        return biggest_sum, biggest_num, inside

x=biggest_loop(10)
print(f'Наибольшее число по сумме цифр является {x[1]}. Сумма цифр {x[0]}.')
print()
#Подсчет занимаемой памяти
sum_1=0

for y in x[2]:
    print(y)
    size=re.search(r'(\d+)',y)
    sum_1+=int(size.group())

print(f'Общая сумма занимаего места = {sum_1}')
print()

print('Вариант_2:')
def biggest_rec(n,biggest_sum=0, biggest_num=0,inside=[]):
    for i in reversed(range(n)):
        #number = int(input("Введите натуральное число: "))
        #number=random.randint(1,1000000)
        number=50-i         #чтобы сравнение было по равным числам
        saved_number=number
        total_sum=0

        inside.extend(show_size(saved_number))           #память переменной

        while number > 0:
            digit=number % 10
            total_sum=total_sum + digit
            number//=10

        if total_sum > biggest_sum:
            biggest_sum = total_sum
            biggest_num = saved_number

            inside.extend(show_size(biggest_sum))               #память переменной
            inside.extend(show_size(biggest_num))        #память переменной

        if i==0:
            return biggest_sum, biggest_num, inside

        biggest_sum, biggest_num,inside = biggest_rec(n-1,biggest_sum, biggest_num, inside)       #Важно запомнить !
        return biggest_sum, biggest_num, inside

x=biggest_rec(10)
print(f'Наибольшее число по сумме цифр является {x[1]}. Сумма цифр {x[0]}.')

#Подсчет занимаемой памяти
sum_2=0

for y in x[2]:
    print(y)
    size=re.search(r'(\d+)',y)
    sum_2+=int(size.group())

print(f'Общая сумма занимаего места = {sum_2}')
print()

print('Вариант_3:')
def biggest_dict(n,biggest_sum=0, biggest_num=0):
    numbers = []
    sums = []
    for i in reversed(range(n)):
        # number = int(input("Введите натуральное число: "))
        #number=random.randint(1,1000000)
        number = 50-i            #чтобы сравнение было по равным числам
        numbers.append(number)
        total_sum = 0
        inside = []

        while number > 0:
            digit = number % 10
            total_sum = total_sum + digit
            number //= 10
        sums.append(total_sum)

        if i == 0:
            l_max=[]
            d = dict(zip(numbers, sums))
            inside.extend(show_size(d))               #память переменной
            for key, val in d.items():
                if not (l_max):
                    l_max.append((key, val))
                elif l_max[0][1] < val:
                    l_max = [(key, val)]
                elif l_max[0][1] == val:
                    l_max.append((key, val))
            inside.extend(show_size(l_max))           #память переменной
            return l_max, inside


x=biggest_dict(10)
print(f'Наибольшее число по сумме цифр является {[i[0] for i in x[0]]}. Сумма цифр {x[0][0][1]}.')

sum_3=0

for y in x[1]:
    print(y)
    size=re.search(r'(\d+)',y)
    sum_3+=int(size.group())

print(f'Общая сумма занимаего места = {sum_3}')
print()