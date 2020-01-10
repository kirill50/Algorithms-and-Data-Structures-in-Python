#Task_1:
def operation(a,b):
   sign=input('Введите знак операции "0", "+", "-", "*", "/":') #0 for exit
   signs=["0", "+", "-", "*", "/"]
   if sign not in signs:
       return operation(a,b)
   elif sign == "/":
       if b==0:
           print('Невозможно деление на "0".')
       else:
           c=a/b
           print(c)
   elif sign == "*":
       c=a*b
       print(c)
   elif sign == "+":
       c=a+b
       print(c)
   elif sign == "-":
       c=a-b
       print(c)
   elif sign == "0":
       print("Программа завершила работу.")
       return

   a = int(input('Введите новое число a:'))
   b = int(input('Введите новое число b:'))
   return operation(a, b)

operation(1,0)
print(" ")

#Task_2:
num=int(input("Введите натуральное число: "))
even=0
odd=0

while num>0:
    check=num%10
    if check%2==0:
        even+=1
    else:
        odd+=1

    num//=10

print(f'В введённое число входит {even} чётных чисел и {odd} нечётных.')
print(" ")

#Task_3:

num=int(input("Введите натуральное число: "))
digits=[]

while num>0:
    digit=num%10
    digits.append(digit)
    num//=10

number = digits[0]
for d in digits[1:]:
    number = 10 * number + d

print(f'Обратное число{number}')
print(" ")

#Task_4:
n=int(input("Введите кол-во элементов последовательности, которые мы будем складывать: "))
number=1
sequence=[]

while n>0:
    n-=1
    sequence.append(number)
    number*=-0.5

print(sequence)
print(f'Сумма всех элементов последовательности равна {sum(sequence)}')
print(" ")

#Task_5:
for i in range(32, 128):
    print("%4d-%s" % (i, chr(i)), end='')
    if i % 10 == 0:
        print()

print()
#Task_6:

import random

hidden_number=random.randint(0,100)
tries=10

while tries>0:
    answer=int(input('Попробуйте отгадать загаданное число:'))
    if answer==hidden_number:
        print(f"Верно, загаданное число {hidden_number}. Вы победили.")
        break
    elif answer<hidden_number:
        print(f"Неверно, загаданное число больше")
        if tries==1:
            print('10 попыток закончилось. Поражение!')
    else:
        print(f"Неверно, загаданное число меньше")
        if tries==1:
            print('10 попыток закончилось. Поражение!')
    tries -= 1

print()
#Task_7:
n = int(input("Введите натуральное число: "))
s = 0
for i in range(1,n+1):
    s += i
m = n * (n + 1) // 2
print(s)
print(m)

print()
#Task_8:
num = int(input("Введите натуральное число: "))
digit=int(input("Введите цифру от 0 до 9 число повторов, которой будем отслеживать: "))
repetition=0

while num>0:
    check=num%10
    if check == digit:
        repetition+=1
    num//=10

print(repetition)
print()

#Task_9:
biggest_sum=0

while True:
    number=int(input("Введите натуральное число: "))
    if number==0:                                      #Выход из цикла, если вводим 0
        break
    num=number
    total_sum = 0
    while number>0:
        digit = number % 10
        total_sum=total_sum+digit
        number //= 10

    if total_sum>biggest_sum:
        biggest_sum=total_sum
        biggest_num=num

print(f'Наибольшее число по сумме цифр является {biggest_num}. Сумма цифр {biggest_sum}.')