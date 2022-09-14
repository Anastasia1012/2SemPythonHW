import time
from random import randint
#1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 
#Учтите, что числа могут быть отрицательными

#Пример:

#67.82 -> 23
#0.56 -> 11

from sre_parse import DIGITS
from string import digits


num = input('input number and find sum') 
num=num.replace('.','') #если число дробное функцией replace удаляем точку(меняем . на '') 
num=int(num) #преобразование в целое число
num = abs(num) #Если число отрицательное, это не влияет на сумму его цифр. 
#В таком случае достаточно будет использовать встроенную в Python функции abc(), 
#которая возвращает абсолютное значение переданного ей аргумента.
sum = 0
while num != 0:
    sum = sum + num % 10 #23%10=3
    num = num // 10#2
print(f'sum=: {sum}')#print('sum = ',sum) #f,format помогает преобразовывать в текст переменную. 
#Вместо sum=: можно написать что угодно.Здесь пишем просто текст(результат и тд)

#2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
#Не используйте функцию math.factorial.
#Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.

#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


try: # в этом цикле проверка корректности выполнения кода, в том числе и на буквы
    n = int(input('Input number n and output mult list'))
 
    factorial = 1
    print(factorial)
    for i in range(2, n+1): #двойка, потому что единицу мы уже учли
        factorial *= i 
        print(factorial)
        # *= Оператор *= сначала умножает значение выражения (справа от оператора)
    #на значение переменной или свойства (слева от оператора). 
    #Затем оператор назначает результат этой операции переменной или свойству.
 
    
except ValueError:
    print('error input')

n = int(input("input n")) 
f = 1

while n > 1:
    f = f * n
    n = n - 1 # от обратного, так как n у нас больше единицы
print(f)

n = int(input("input n")) 
f = 1

for i in range(2, n+1):
    f = f * i
print(f)
 

#3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

#N = int(input('input number = qty of elements')) 
#a = list() 
 
#result = 0 
#for i in range(1, N+1): 
#    result += (1 + 1/i)**i #возведение в степень 1,5*1,5=2,25
#print(round(result, 2))


#3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
#А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
#Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
#Это происходит до тех пор, пока не будет найден палиндром.
#Напишите такую программу, которая найдет палиндром введенного пользователем числа.

def check_pal(n):
    res = 0
    while n != 0:
        digit=n%10
        res = res*10+digit 
        n = n//10
    return res
    
try:
    num = int(input('input number and check palindrom'))
    palindrom = check_pal(num)
    if num == palindrom:
        print('input number is palindrom')
    else:
        while num != palindrom:
            num = num + palindrom
            palindrom=check_pal(num)
        print(f'output palindrom {num}')

except ValueError:
    print('error')



#4 - Реализуйте выдачу случайного числа
#не использовать random.randint и вообще библиотеку random
#Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
#Учтите, что есть диапазон: от(минимальное) и до (максимальное)


number = randint(1, 5)
arr=(int(str(time.time())[-number:])) 
print(*arr)
print(time.time())
