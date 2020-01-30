#1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный
# случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
#Примечания:
#a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
#b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random, time

print("Задача №1")

size=10
array=[random.randint(-100,100) for i in range(size)]
print(array)

def sorted_by_buble(array):
    n=1
    while n<len(array):
        count = 0          #чтобы мы не делали итераций по циклу, когда уже все отсортировано, я добавил эту переменную
        for i in range(len(array)-n):
            if array[i]<array[i+1]:
                count+=1
                array[i], array[i+1]=array[i+1],array[i]
        if count==0:      #когда if array[i]<array[i+1]: ни разу in range не сработала это значит, что уже все отсортировано
            return
        n+=1

sorted_by_buble(array)
print(array)
print()
time.sleep(0.5)
#2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

print("Задача №2")

size=10
array=[random.randint(0,49) for i in range(size)]
print(array)

def sorted_by_merge(array):
    if len(array)>1:
        mid=len(array)//2
        lefthalf=array[:mid]
        righthalf=array[mid:]

        sorted_by_merge(lefthalf)
        sorted_by_merge(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i = i + 1
            else:
                array[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j = j + 1
            k = k + 1

sorted_by_merge(array)
print(array)
print()
time.sleep(0.5)

#3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
#Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

print("Задача №3")

size=11
array=[2*random.randint(-100,100)+1 for m in range(size)]
print(array)

def nearest(array,size):
    minimum_number=min(array)
    if size%2==0:
        index_1 = int(size/2)
        for i in range(index_1-1):
            number_remove = min(array, key=lambda x: abs(x - minimum_number))
            array.remove(number_remove)
        number = min(array, key=lambda x: abs(x - minimum_number))
        array.remove(number)
        number_2 = min(array, key=lambda x: abs(x - minimum_number))
        return (number_2+number)/2
    else:
        index=int((size-1)/2+1)
        for i in range(index-1):
            number_remove=min(array, key=lambda x: abs(x - minimum_number))
            array.remove(number_remove)
        number=min(array, key=lambda x: abs(x - minimum_number))
        return number

x=nearest(array,size)
print(f'Медиана = {x}')