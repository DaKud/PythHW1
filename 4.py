# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти
#  (x и y).

quarter_number = int(input('Insert quarter number:'))

if quarter_number == 1:
    print('X>0, Y>0')
if quarter_number == 2:
    print('X<0, Y>0')
if quarter_number == 3:
    print('X<0, Y<0')
if quarter_number == 4:
    print('X>0, Y>0')
