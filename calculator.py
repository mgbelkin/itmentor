####################################################################################################
# главная ф-я программы, на вход - строка, на выход - результат вычисления

def main(s):
    massive = s.split()
    a = int(massive[0])
    b = int(massive[2])
    if massive[1] == "+":
        return a + b
    elif massive[1] == "-":
        return a - b
    elif massive[1] == "*":
        return a * b
    else:
        return a // b


############################################################################
# ф-я которая проверяет соответствие заданному формату

def if_everything_correct(s):
    correctflag = False

    if s.startswith(' ') or s.endswith(' '):  # если есть пробелы в конце или в начале - сразу на выход
        return correctflag
    elif s.count(' ') != 2:  # если пробелов НЕ два - на выход
        return correctflag

    massive = s.split()  # создаем список из строки, разбивая по пробелам
    if len(massive) != 3:  # если число элементов не 3 - на выход
        return correctflag
    elif massive[1] not in "+-*/":  # если нет арифмет д-й - на выход
        return correctflag
    elif massive[0].isdigit() == False or massive[2].isdigit() == False:  # проверяем ввели ли ЦЕЛЫЕ числа
        return correctflag
    elif (int(massive[0]) < 1 or int(massive[0]) > 10) or (
            int(massive[2]) < 1 or int(massive[2]) > 10):  # проверка чисел на соотв-е интервалу [1; 10]
        return correctflag

    else:
        correctflag = True
        return correctflag



#################################################################################
# основная программа

print("Введите задачу на вычисление в формате [число][пробел][знак операции][пробел][число]")
print()

s = input()

t = if_everything_correct(s)
if t == False:
    print("Неверный формат ввода")
else:
    print(main(s))

exit