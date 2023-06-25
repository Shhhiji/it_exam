import function

if __name__ == '__main__':
    while True:
        try:
            print("Площадь прямоугольника\n\nДля остановки работы программы нажмите ctrl+z+Enter или ctrl+c\n")
            a = input("Введите длину прямоугольника в см : ")
            b = input("\nВведите ширину прямоугольника в см : ")
            a, error_str = function.oknumber(a)
            error = False
            if error_str is not None:
                print(error_str)
                error = True
            b, error_str = function.oknumber(b)
            if error_str is not None:
                print(error_str)
                error = True
            if error:
                continue
            result = function.spryamoyg(a, b)
            print("\nПлощадь вашего прямоугольника в квадратных сантиметрах равна : ","{:.2f}".format(result))
        except EOFError:
            print("Завершение работы программы. До новых встреч)")
            break
        except KeyboardInterrupt:
            print('\nЗавершение работы программы. До новых вычислений')
            break


# def spryamoyg(a, b): # Площадь прямоугольника
#     s = a*b
#     return s

# def oknumber(num:str): # Проверка что ввел пользователь число или строку
#     number = None
#     error_str = None
#     if not isNumber(num):
#         error_str = 'Вы ввели не числовое значение {}. Попробуйте снова\n'.format(num)
#     else:
#         num = float(num)
#         if num <= 0:
#             error_str = 'Вы ввели число {} меньше нуля или равное нулю. Попробуйте снова!\n'.format(num)
#         else:
#             number = num
#     return number, error_str

# def isNumber(element): # Функция для проверки ввода пользователем числа числа с плавающей точкой
#     result = True
#     try:
#         float(element)
#     except ValueError:
#         result = False
#     finally:
#         return result