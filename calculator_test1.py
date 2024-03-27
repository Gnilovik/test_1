def main(input_x: str) -> str:
    try:
        a, c, b = input_x.split()
        a = int(a)
        b = int(b)
        if 1 <= a <= 10 and 1 <= b <=10 and c == '+':
            return a+b
        elif 1 <= a <= 10 and 1 <= b <=10 and c == '-':
            return a-b
        elif 1 <= a <= 10 and 1 <= b <=10 and c == '*':
            return a*b
        elif a==0 or b==0 and c=='/':
            return 'На ноль делить нельзя!'
        elif 1 <= a <= 10 and 1 <= b <=10 and c == '/':
            return a//b
        else:
            return 'Принимаются цифры от 1 до 10!'
    except ValueError:
        return 'Формат математической операции не верный!'

input_x = input("Введите числа: ")
print(main(input_x))