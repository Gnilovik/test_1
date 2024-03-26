try:
    a, c, b = input('Введите числа:').split()
    a = int(a)
    b = int(b)
    if 1 <= a <= 10 and 1 <= b <=10 and c == '+':
        print(a+b)
    elif 1 <= a <= 10 and 1 <= b <=10 and c == '-':
        print(a-b)
    elif 1 <= a <= 10 and 1 <= b <=10 and c == '*':
        print(a*b)
    elif a==0 or b==0 and c=='/':
        print('На ноль делить нельзя!')
    elif 1 <= a <= 10 and 1 <= b <=10 and c == '/':
        print(a//b)
    else:
        print('Не верно!')
except Exception:
    print('Формат математической операции не верный!')