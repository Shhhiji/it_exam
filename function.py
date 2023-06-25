import math

def isNumber(element): # Функция для проверки ввода пользователем числа числа с плавающей точкой
    result = True
    try:
        float(element)
    except ValueError:
        result = False
    finally:
        return result
    
def spryamoyg(a, b): # Площадь прямоугольника
    s = a*b
    return s

def oknumber(num:str): # Проверка что ввел пользователь число или строку
    number = None
    error_str = None
    if not isNumber(num):
        error_str = 'Вы ввели не числовое значение {}. Попробуйте снова\n'.format(num)
    else:
        num = float(num)
        if num <= 0:
            error_str = 'Вы ввели число {} меньше нуля или равное нулю. Попробуйте снова!\n'.format(num)
        else:
            number = num
    return number, error_str


def area_rad(radius): # Площадь круга через радиус
    return radius**2*math.pi

def area_diam(diameter): # Площадь круга через диаметер
    return (diameter/2)**2*math.pi

def isNumberint(element): # Функция для проверки ввода пользователем целого числа
    result = True
    try:
        int(element)
    except ValueError:
        result = False
    finally:
        return result
    
    
import random

def ran(n, bot, top): # Генерируем рандомно числа из заданного промежутка и считаем кол-во отриц чисел
    numbers = []
    neg = 0
    for i in range(n):
        numbers.append(random.randint(bot, top))
    for i in numbers:
        if i < 0:
            neg = neg+1
    return numbers, neg

def ranpos(n, bot, top): # Генерируем рандомно числа из заданного промежутка и считаем кол-во + чисел
    numbers = []
    pos = 0
    for i in range(n):
        numbers.append(random.randint(bot, top))
    for i in numbers:
        if i > 0:
            pos = pos+1
    return numbers, pos

def sumneg(n, bot, top): # Генерируем рандомно числа из заданного промежутка и считаем сумму отриц чисел
    numbers = []
    neg = []
    for i in range(n):
        numbers.append(random.randint(bot, top))
    for i in numbers:
        if i < 0:
            neg.append(i)
            summa = sum(neg)
    return numbers, summa

def sumpos(n, bot, top): # Генерируем рандомно числа из заданного промежутка и считаем сумму + чисел
    numbers = []
    pos = []
    for i in range(n):
        numbers.append(random.randint(bot, top))
    for i in numbers:
        if i > 0:
            pos.append(i)
        summa = sum(pos)
    return numbers, summa

def arifmetic(n, bot, top): # Генерируем рандомно числа из заданного промежутка и считаем среднеарифметическое чисел больше 10
    numbers = []
    pos = []
    for i in range(n):
        numbers.append(random.randint(bot, top))
    for i in numbers:
        if i >= 10:
            pos.append(i)
    summa = sum(pos)
    leng = len(pos)
    arif = summa/leng
    return numbers, arif

from statistics import median # вызов функции для посчета медианы

def median_num(n, bot, top): # Генерируем рандомно числа из заданного промежутка и считаем медиану чисел
    numbers = []
    for i in range(n):
        numbers.append(random.randint(bot, top))
    res = median(numbers)
    return numbers, res


from statistics import mean

def arif(n, bot, top): # Генерируем рандомно числа из заданного промежутка и считаем среднеарифметическое + чисел 
    numbers = []
    pos = []
    for i in range(n):
        numbers.append(random.randint(bot, top))
    for i in numbers:
        if i > 0:
            pos.append(i)
    ar = mean(pos)
    return numbers, ar

def max_num(n, bot, top): # Генерируем рандомно числа из заданного промежутка и ищем мах число
    numbers = []
    for i in range(n):
        numbers.append(random.randint(bot, top))
    res = max(numbers)
    return numbers, res

def num_up(n, bot, top): # Генерируем рандомно числа из заданного промежутка и ссортируем в порядке возрастания
    numbers = []
    for i in range(n):
        numbers.append(random.randint(bot, top))
    res = sorted(numbers)
    return numbers, res

def num_down(n, bot, top): # Генерируем рандомно числа из заданного промежутка и ссортируем в порядке убывания
    numbers = []
    for i in range(n):
        numbers.append(random.randint(bot, top))
    res = sorted(numbers, reverse=True)
    return numbers, res

def schet(num_list): # Функция отвечающая за счет среднего значения
    sum_num = 0
    for x in num_list:
        sum_num = sum_num + x
    avg = sum_num / len(num_list)
    return avg

def mult(num_list): # Функция отвечающая за счет произведения чисел
    mult_num = 1
    for x in num_list:
        mult_num = mult_num * x
    return mult_num

def summa(num_list): # Функция отвечающая за счет произведения чисел
    sum_num = 0
    for x in num_list:
        sum_num = sum_num + x
    return sum_num

def med(num_list): # Функция отвечающая за подсчет медианы чисел
    res = median(num_list)
    return res
    
    
import re

def str_list(): # Функция для ввода пользователем любого текста и выход из программы
    exitStr = "\x1a" # hex код сочетания ctrl+z
    list_ent = list()
    try:
        print('Замена букв в тексте пользователя.')
        while True:
            print('\nДля вывода результата нажмите ctrl+z+Еnter')
            print('Для завершения работы программы нажмите ctrl+c')
            ent = input('\nВведите ваше сообщение : ')
            if ent.__contains__(exitStr): # проверка содержит ли строка crl+z 
                ent = ent.split(exitStr)[0]
                list_ent.append(ent)
                break
            else:
                list_ent.append(ent)
    except EOFError:
        print('\nВывод результата...')
    return list_ent



def zamena(list_ent): # Функция для замены символов
    ret = [] 
    for i in list_ent:
        i_n = re.sub("л|Л", "!!!!", i)
        ret.append(i_n)
    return ret


    
def povtor(num, strok):
    for i in range(num):
        print(strok)

def oknum(num:str): # Проверка что ввел пользователь число или строку
    number = None
    error_str = None
    if not isNumber(num):
        error_str = '\nВы ввели не числовое значение {}. Попробуйте снова\n'.format(num)
    elif not isNumberint(num):
        error_str = '\nВы ввели не целое значение {}. Попробуйте снова\n'.format(num)
    else:
        num = int(num)
        if num <= 0:
            error_str = 'Вы ввели число {} меньше нуля или равное нулю. Попробуйте снова!\n'.format(num)
        else:
            number = num
    return number, error_str