# Напишите программу, которая принимает на вход 
# координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

X = int(input('Insert X:'))
Y = int(input('Insert Y:'))

if X>0 and Y>0:
    print('1st quarter')
if X<0 and Y>0:
    print('2nd quarter')
if X<0 and Y<0:
    print('3rd quarter')
if X>0 and Y<0:
    print('4th quarter')
