# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет,
# является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет



dayofweek = int(input('Insert day number(starts with Mon=1, end with Sund=7):'))
if dayofweek < 6:
    print('NOPE')
elif dayofweek == 6 :
    print('YEP')
elif dayofweek == 7 :
    print('YEP')   
else:
    print('stop')