#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def is_number(n):                                                                                   #Проверка на float
    try:
        float(n)
    except ValueError:
        return False
    else:
        return True


def stry():                                                                                         #Повтор строки n раз
    s1 = raw_input('Введите строку: ')
    try:
        n = int(raw_input('Введите количество повторов: '))
    except ValueError:
        print('Ошибка во входных данных')
        return 0
    print (s1 * n)


def strs():                                                                                         #Конкатенация
    s3 = raw_input("Введите первую строку: ")
    s2 = raw_input("Введите вторую строку: ")
    print (s3 + s2)


def sinus():                                                                                        #Синус градусов
    n = raw_input('Введите градусную меру: ')
    if is_number(n):
        print('Синус этого угла равен ' + str(math.sin(math.radians(float(n)))))
    else:
        print('Ошибка во входных данных')


def cosinus():                                                                                      #Косинус градусов
    n = raw_input('Введите градусную меру: ')
    if is_number(n):
        print('Синус этого угла равен ' + str(math.cos(math.radians(float(n)))))
    else:
        print('Ошибка во входных данных')


def ten_to_16():                                                                                    #Перевод из 10 СС в 16 СС
    n = raw_input('Введите число для перевода в шестнадцатеричную систему: ')
    try:
        n = int(n)
    except ValueError:
        print ('Это не число!')
    else:
        ans = hex(n)
        if n < 0:
            print (ans[0] + ans[3:]).upper()
        else:
            print ans[2:].upper()


def q():                                                                                           # Меню бинарных операций
    c = raw_input('Выберите бинарную операцию над числами (\"&\", \"|\" или \"!\"): ')
    if c == '&':
        and_func()
    elif c == '|':
        or_func()
    elif c == '!':
        not_func()
    else:
        print('Ошибка во входных данных')


def and_func():                                                                                    # Бинарная операция "И"
    try:
        a = int(raw_input('Введите первую переменную: '))
        b = int(raw_input('Введите вторую переменную: '))
    except ValueError:
        print('Ошибка во входных данных')
        return 0
    if a >= 0 and b >= 0:
        print(a & b)
    else:
        print('Невозможно применить к отрицательным числам')


def or_func():                                                                                     # Бинарная операция "ИЛИ"
    try:
        a = int(raw_input('Введите первую переменную: '))
        b = int(raw_input('Введите вторую переменную: '))
    except ValueError:
        print('Ошибка во входных данных')
        return 0
    if a >= 0 and b >= 0:
        print(a | b)
    else:
        print('Невозможно применить к отрицательным числам')


def not_func():                                                                                    # Бинарная операция "НЕ"
    try:
        a = int(raw_input('Введите первую переменную: '))
    except ValueError:
        print('Ошибка во входных данных')
        return 0
    if a >= 0:
        print(~a)
    else:
        print('Неозможно применить к отрицательным числам')


def ten_to_binary():                                                                               # Перевод из 10 СС в 2 СС
    a = raw_input('Введите число в десятичной системе счисления: ')
    s = a
    if a[0] == '-':
        s = a[1:]

    while not s.isdigit():
        a = raw_input('Введенная строка не является числом. Введите число в десятичной системе счисления повторно: ')
        s = a
        if a[0] == '-':
            s = a[1:]

    a = int(a)
    ans = str(bin(a))
    print 'Число в двоичной системе счисления: ', ans[0:(a < 0)] + ans[2 + (a < 0):]


def ten_to_eight():                                                                                # Перевод из 10 СС в 8 СС
    n = int(input("Введите число в десятичной системе счисления: ",))
    a = []
    if 0 <= n < 8:
        print "Ответ: " + str(n)
        return 0
    sign = ''
    if n < 0:
        sign = '-'
        n = -n

    while n >= 8:
        a.append(n % 8)
        n //= 8
    a.append(n)
    print 'Ответ: ' + sign + ''.join([str(c) for c in a[::-1]])


def ffff():                                                                                         #Сложение/вычитание/умножение/деление чисел
    a = raw_input('Выберите операцию (\"+\", \"-\", \"*\" или \"/\"): ')
    try:
        b = float(raw_input('Введите первое число: '))
        c = float(raw_input('Введите второе число: '))
    except ValueError:
        print('Ошибка во входных данных')
        return
    if a == '+':
        print(b+c)
    elif a == '-':
        print(b-c)
    elif a == '*':
        print(b*c)
    elif a == '/':
        if c == 0:
            print('На ноль делить нельзя!')
        else:
            print(b/c)


def cosrad():                                                                                     #Косинус радиан
    try:
        a = float(raw_input('Введите число в радианах: '))
    except ValueError:
        print('Ошибка во входных данных')
        return 0
    print math.cos(a)


def sinrad():                                                                                      #Синус радиан
    try:
        b = float(raw_input('Введите число в радианах: '))
    except ValueError:
        print('Ошибка во входных данных')
        return 0
    print math.sin(b)


def sqrtab():                                                                                      #Произвольный корень числа
    num1 = raw_input("Введите число, из которого будет извлекаться корень: ")
    num2 = raw_input("Введите степень корня: ")
    if is_number(num1) and is_number(num2):
        print ("Корень {0} степени из числа {1} равен {2}".format(num2, num1, float(num1)**(1/float(num2))))
    else:
        print('Ошибка во входных данных')


def stepab():                                                                                      #Возведение числа в произвольную степень
    num1 = raw_input("Введите число, которое будет возводиться в степень: ")
    num2 = raw_input("Введите степень: ")
    if is_number(num1) and is_number(num2):
        print ("{0}ая степень числа {1} равна {2}".format(num2, num1, float(num1)**float(num2)))
    else:
        print('Ошибка во входных данных')


def modab():                                                                                       #Остаток от деления 
    num1 = raw_input("Введите число, из которого будет вычисляться остаток от деления: ")
    num2 = raw_input("Введите число, на которое будет делиться число: ")
    if is_number(num1) and is_number(num2):
        print ("Остаток от деления числа {0} на число {1} равен {2}".format(num1, num2, float(num1) % float(num2)))
    else:
        print('Ошибка во входных данных')


def slov_v_stroke():                                                                               # Подсчет количества слов в строке
    a=str(raw_input("Введите строку: "))
    if len(a) != 0:
        c = 'В этой строке '+str(len(a.split(' ')))+' cлов(а)'
    else:
        c = "Вы не ввели ни одного слова!"
    print(c)
    return 0


def long_multiply(a, b):                                                                           # Умножение длинных чисел
    a.reverse()
    b.reverse()
    c = [0] * (len(a) + len(b) + 1)
    for i in range(len(a)):
        for j in range(len(b)):
            multiply = a[i] * b[j]
            c[i + j] += multiply % 10
            c[i + j + 1] += multiply // 10
    for i in range(len(c) - 1):
        c[i + 1] += c[i] // 10
        c[i] %= 10
    while len(c) > 1 and c[len(c) - 1] == 0:
        c.pop()
    print ''.join([str(i) for i in reversed(c)])


def long_num_add_sub(a, b, f):                                                                     # Сложение/вычитание длинных чисел
    Ans = []
    _lesseq = True
    if not f:
        if len(a) > len(b):
            _lesseq = False
        elif len(a) == len(b):
            for i in range(len(a)):
                if a[i] > b[i]:
                    _lesseq = False
                    break
            _lesseq = False
    a.reverse()
    b.reverse()
    sign = True
    if _lesseq:
        sign = False
        a, b = b, a
    if f:
        for i in range(max(len(a), len(b))):
            cur = 0
            if i < len(b):
                cur += b[i]
            if i < len(a):
                cur += a[i]
            Ans.append(cur)
        for i in range(len(Ans) - 1):
            Ans[i + 1] += Ans[i] // 10
            Ans[i] %= 10
        while Ans[len(Ans) - 1] > 10:
            Ans.append(Ans[len(Ans) - 1] // 10)
            Ans[len(Ans) - 1] %= 10
        Ans.reverse()
    else:
        for i in range(len(b)):
            Ans.append(a[i] - b[i])
        for i in range(len(b) + 1, len(a)):
            Ans.append(a[i])
        for i in range(len(Ans) - 1):
            while Ans[i] < 0:
                Ans[i] += 10
                Ans[i + 1] -= 1
        while len(Ans) > 1 and Ans[len(Ans) - 1] == 0:
            Ans.pop()
        if not sign:
            Ans.append('-')
        Ans.reverse()
    print ''.join(map(str, Ans))


def long_arithmetics():                                                                          # Меню работы с длинными числами
    print "Доступные пункты меню:"
    print "0. Выход"
    print "1. Сложение/вычитание"
    print "2. Умножение"
    f = raw_input()
    if not (f.isdigit()):
        print "Неверный формат ввода!"
        return
    f = int(f)
    if f == 0:
        return
    if f != 1 and f != 2:
        print "Неверный формат ввода!"
        return
    if f == 1:
        print "Введите два числа в формате: [число] (+/-) [число]"
        A = map(str, raw_input().split())
        if len(A) != 3 or not (A[0].isdigit()) or A[1] != '+' and A[1] != '-' or not (A[2].isdigit()) or not (
                A[2][0].isdigit()) or not (A[0][0].isdigit()):
            print "Неверный формат ввода!"
            return
        a = []
        b = []
        for i in range(len(A[0])):
            a.append(int(A[0][i]))
        for i in range(len(A[2])):
            b.append(int(A[2][i]))
        long_num_add_sub(a, b, A[1] == '+')
    elif f == 2:
        print "Введите два числа в формате: [число] * [число]"
        A = map(str, raw_input().split())
        if len(A) != 3 or not (A[0].isdigit()) or A[1] != '*' or not (A[2].isdigit()) or not (
                A[2][0].isdigit()) or not (A[0][0].isdigit()):
            print "Неверный формат ввода!"
            return
        a = []
        b = []
        for i in range(len(A[0])):
            a.append(int(A[0][i]))
        for i in range(len(A[2])):
            b.append(int(A[2][i]))
        long_multiply(a, b)
    return


numbers = [('1. Сложение/вычитание/умножение/деление', ffff),
           ('2. Возведение числа в произвольную степень', stepab),
           ('3. Произвольный корень числа', sqrtab),
           ('4. Остаток от деления', modab),
           ('5. Синус градусов', sinus),
           ('6. Косинус градусов', cosinus),
           ('7. Синус радиан', sinrad),
           ('8. Косинус радиан', cosrad),
           ('9. Бинарные операции', q),
           ('10. 10 -> 2', ten_to_binary),
           ('11. 10 -> 8', ten_to_eight),
           ('12. 10 -> 16', ten_to_16)]                                                            #Меню

strings = [('1. Количество слов в строке', slov_v_stroke),
           ('2. Умножение строк', stry),
           ('3. Сложение строк', strs)]

mode_choose = True

modes = [('0. Выйти', None), ('1. Калькулятор чисел',  numbers), ('2. Калькулятор строк', strings ), ('3. Длинная арифметика', None)]

while True:
    if mode_choose is True:

        while True:
            for i in modes:
                print i[0]
            try:
                choice = input()
            except Exception:
                pass
            else:
                if choice <= len(modes) and choice >= 0:
                    break

        mode_choose = False

    if choice == 0:
        break

    if choice == 3:
        long_arithmetics()
        mode_choose = True
        continue

    print "\nВыберите режим:\n\n0. Назад"

    array = modes[choice][1]

    for i in array:
        print i[0]
    try:
        choice2 = int(raw_input())
    except ValueError:
        continue

    if choice2 < 0 or choice2 > len(array):
        continue
    elif choice2 == 0:
        mode_choose = True
        continue

    array[choice2 - 1][1]()

print ("Спасибо за использование нашего калькулятора!")
