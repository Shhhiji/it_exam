import function

if __name__ == '__main__':
    while True:
        try:
            print("Площадь круга\n\nДля остановки работы программы нажмите ctrl+z+Enter или ctrl+c\n")
            radius = input("Введите радиус круга в см : ")
            radius, error_str = function.oknumber(radius)
            if error_str is not None:
                print(error_str)
                continue
            area_c = function.area_rad(radius)
            if area_c is not None: # если пользователь ввел все что удовлетворяет проверке, то вывод результата
                print("Площадь круга в квадратных сантиметрах : ", "{:.2f}".format(area_c))
                print(" ")
        except EOFError:
            print("Завершение работы программы. До новых встреч)")
            break
        except KeyboardInterrupt:
            print('\nЗавершение работы программы. До новых вычислений')
            break
        
        
# def area_rad(radius): # Площадь круга через радиус
#     return radius**2*math.pi

# def isNumber(element): # Функция для проверки ввода пользователем числа числа с плавающей точкой
#     result = True
#     try:
#         float(element)
#     except ValueError:
#         result = False
#     finally:
#         return result
    
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