# Рабочий пример

# input_string = input()

# a, c, b = input_string.split()
# a = int(a)
# b = int(b)

# if b==0 and c=="/":
#     print("На ноль делить нельзя!")
# elif c!="+" and c!="-" and c!="" and c!="/":
#     print("Неверная операция")
# elif c=="+":
#     print(a+b)
# elif c=="-":
#     print(a-b)
# elif c=="":
#     print(a*b)
# else:
#     print(a/b)


# Пример
# if a != 1 or a != 2 or a != 3 or a != 4 or a != 5 or a != 6 or a != 7 or a != 8 or a != 9 or a != 10 or b != 1 or b != 2 or b != 3 or b != 4 or b != 5 or b != 6 or b != 7 or b != 8 or b != 9 or b != 10:
#    print('Не верная операция')

#def slova(a,b):
#    x = str(a)
#    y = str(b)
#    c = str(c)

# a, c, b = input('Введите числа:').split()
# a = int(a)
# b = int(b)
# if a != int(a) or b != int(b) or c != str(c):
#    print('Слова вводить нельзя')
# elif 1 <= a <= 10 and 1 <= b <=10 and c == '+':
#    print(a+b)
# elif 1 <= a <= 10 and 1 <= b <=10 and c == '-':
#    print(a-b)
# elif 1 <= a <= 10 and 1 <= b <=10 and c == '*':
#    print(a*b)
# elif a==0 or b==0 and c=='/':
#    print('На ноль делить нельзя!')
# elif 1 <= a <= 10 and 1 <= b <=10 and c == '/':
#    print(a/b)
# else:
#    print('Не верно!')



# ЭТО ПРАВИЛЬНЫЙ КАЛЬКУЛЯТОР 


# not any(char in input_string for char in ['+', '-', '*', '/'])
# input_string = input("Введите выражение (например, '3 + 5'): ")
# if not any(char in input_string for char in ['+', '-', '', '/']):
#     print("Не вижу цифр, я калькулятор а не блокнот")
# else:
#     a, c, b = input_string.strip().split()
#     a = int(a)
#     b = int(b)
#     if b==0 and c=="/":
#         print("На ноль делить нельзя!")
#     elif a < 1 or a > 10 or b < 1 or b > 10:
#         print("Числа должны быть от 1 до 10")
#     elif c=="+":
#         print(a+b)
#     elif c=="-":
#         print(a-b)
#     elif c=="":

try:
    a, c, b = input('Введите числа:').split()
    a = int(a)
    b = int(b)
    if 1 <= a <= 10 and 1 <= b <=10 and c == '+':
        print(a+b)
