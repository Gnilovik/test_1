# try:
#     a, c, b = input('Введите числа:').split()
#     a = int(a)
#     b = int(b)
#     if 1 <= a <= 10 and 1 <= b <=10 and c == '+':
#         print(a+b)
#     elif 1 <= a <= 10 and 1 <= b <=10 and c == '-':
#         print(a-b)
#     elif 1 <= a <= 10 and 1 <= b <=10 and c == '*':
#         print(a*b)
#     elif a==0 or b==0 and c=='/':
#         print('На ноль делить нельзя!')
#     elif 1 <= a <= 10 and 1 <= b <=10 and c == '/':
#         print(a//b)
#     else:
#         print('Не верно!')
# except Exception:
#     print('Формат математической операции не верный!')


def main(input: str) -> str:
    try:
        operation = input.split()[1]
        a = int(input.split()[0])
        b = int(input.split()[2])

        if a < 1 or a > 10 or b < 1 or b > 10:
            raise ValueError("Числа должны быть от 1 до 10")

        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            return a // b
        else:
            raise ValueError("Неправильная операция")

#        return str(return)
    
    except (ValueError, ZeroDivisionError) as e:
        return str(e)
    
input = input("Введите выражение для вычисления (например, '5 + 3'): ")
print(main(input))