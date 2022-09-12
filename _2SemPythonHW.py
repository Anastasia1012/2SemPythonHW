import time
from random import randint
#1 - �������� ���������, ������� ��������� �� ���� ������������ ����� � ���������� ����� ��� ����. 
#������, ��� ����� ����� ���� ��������������

#������:

#67.82 -> 23
#0.56 -> 11

from sre_parse import DIGITS
from string import digits


num = input('input number and find sum') 
num=num.replace('.','') #���� ����� ������� �������� replace ������� �����(������ . �� '') 
num=int(num) #�������������� � ����� �����
num = abs(num) #���� ����� �������������, ��� �� ������ �� ����� ��� ����. 
#� ����� ������ ���������� ����� ������������ ���������� � Python ������� abc(), 
#������� ���������� ���������� �������� ����������� �� ���������.
sum = 0
while num != 0:
    sum = sum + num % 10 #23%10=3
    num = num // 10#2
print(f'sum=: {sum}')#print('sum = ',sum) #f,format �������� ��������������� � ����� ����������. 
#������ sum=: ����� �������� ��� ������.����� ����� ������ �����(��������� � ��)

#2 - �������� ���������, ������� ��������� �� ���� ����� N � ������ ����� ������������ (����� - ��� ������) ����� �� 1 �� N.
#�� ����������� ������� math.factorial.
#�������� �������� ����� N: ����� ������������ �� ��� ������ �����.

#������:
#- ����� N = 4, ����� [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


try: # � ���� ����� �������� ������������ ���������� ����, � ��� ����� � �� �����
    n = int(input('Input number n and output mult list'))
 
    factorial = 1
    print(factorial)
    for i in range(2, n+1): #������, ������ ��� ������� �� ��� ����
        factorial *= i 
        print(factorial)
        # *= �������� *= ������� �������� �������� ��������� (������ �� ���������)
    #�� �������� ���������� ��� �������� (����� �� ���������). 
    #����� �������� ��������� ��������� ���� �������� ���������� ��� ��������.
 
    
except ValueError:
    print('error input')

n = int(input("input n")) 
f = 1

while n > 1:
    f = f * n
    n = n - 1 # �� ���������, ��� ��� n � ��� ������ �������
print(f)

n = int(input("input n")) 
f = 1

for i in range(2, n+1):
    f = f * i
print(f)
 

#3.������� ������ �� n ����� ������������������ $(1+\frac 1 n)^n$ � �������� �� ����� �� �����.

#N = int(input('input number = qty of elements')) 
#a = list() 
 
#result = 0 
#for i in range(1, N+1): 
#    result += (1 + 1/i)**i #���������� � ������� 1,5*1,5=2,25
#print(round(result, 2))


#3 - ����������� ���������� �����, ������� � ��� ������� �������� ���������: "�����", "�����".
#� ��� ���� ��������� ����� - ����� ����� � ���, ����� ����� � ��� ������� �������� ���������, �� ���� ���� "��".
#���� ������������ ����� �� ����� ���������, �� ��� ������������ � ����������� �� ��������� ��� ���.
#��� ���������� �� ��� ���, ���� �� ����� ������ ���������.
#�������� ����� ���������, ������� ������ ��������� ���������� ������������� �����.

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



#4 - ���������� ������ ���������� �����
#�� ������������ random.randint � ������ ���������� random
#������ ������������ xor, ����, ���������� time ��� datetime (������������ ��� �����������) - ��� ������� �����������
#������, ��� ���� ��������: ��(�����������) � �� (������������)


arr = list()
for i in range(10):
    number = randint(1, 5)
time.sleep(1)
arr.append(int(str(time.time())[-number:]))
print(*arr)