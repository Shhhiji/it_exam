# # import Heron # Импорт модуля из файла
# # from error import isPositivNumber # Импорт модуля возможно возникших ошибок из файла

# # основной модуль

# if __name__ == "__main__": 
#     while True:
#         try:
#             print("Это точно треугольник?\n")
#             a = input('Введите сторону 1 : ')
#             res, error = isPositivNumber(a)
#             if(not res):
#                 print(error)
#                 continue
#             b = input('Введите сторону 2 : ')
#             res, error = isPositivNumber(b)
#             if(not res):
#                 print(error)
#                 continue
#             c = input('Введите сторону 3 : ')
#             res, error = isPositivNumber(c)
#             if(not res):
#                 print(error)
#                 continue
#             a = float(a)
#             b = float(b)
#             c = float(c)
#             res, error = Heron.check(a, b, c) # проверка, что треугольник существует
#             if res:
#                 result = Heron.process(a,b,c)
#                 print("\nПлощадь треугольника равна : ", "{:.2f}".format(result))
#             else:
#                 print(error)
#         except KeyboardInterrupt: # Выход из программы сочетанием клавиш ctrl+c
#             print("\nЗавершение работы. \nДо новых встреч и вычислений)))")
#             break
#         except EOFError: # Выход из программы сочетанием клавиш ctrl+z+Enter
#             print("Завершение работы. \nДо новых встреч и вычислений :)")
#             break
#         print("\nЧтобы выйти из программы нажмите ctrl+c или ctrl+z+Enter\n")






# Модуль с проверками

# import math

# def check(a, b, c):
#     res = False
#     error = None
#     if a + b > c:
#         if a + c > b:
#             if b + c > a:
#                 res = True
#             else:
#                 error = "\nОшибка в стороне 1 = {} Попытайтесь ввести значения снова :)".format(a)
#         else:
#             error = "\nОшибка в стороне 2 = {} Попытайтесь ввести значения снова :)".format(b)
#     else:
#        error = "\nОшибка в стороне 3 = {} Попытайтесь ввести значения снова :)".format(c)
#     return res, error

# def process(a, b, c):  # Функция расчета площади треугольника по формуле Герона
#     pol = (a + b + c)/2  # Полупериметр
#     area = math.sqrt(((pol-a)*(pol-b)*(pol-c))*pol) # формула Герона
#     return area

# def isNumber(element): # Функция для проверки ввода пользователем числа числа с плавающей точкой
#     result = True
#     try:
#         float(element)
#     except ValueError:
#         result = False
#     finally:
#         return result

# def isPositivNumber(num):
#     if(not isNumber(num)):
#         return False, "Вы ввели {} не число! Попробуйте снова!".format(num)
#     num = float(num)
#     if(num > 0):
#         return True, None
#     else:
#         return False, "Вы ввели {} отрицательное число или ноль. Попытайтесь снова!".format(num)