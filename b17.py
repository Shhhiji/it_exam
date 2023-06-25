import function

if __name__ == '__main__':
    try:
        while True:
            while True:
                averg_str = input("Сумма чисел.\nВведите числовые значения через пробел: ").split()
                if len(averg_str) == 0: # Проверка, что пользователь ничего не ввел
                    print("\nВы не ввели никаких чисел! Попробуйте снова.\n")
                else:
                    averg = list()
                    haserrors = False
                    for i in averg_str:
                        if function.isNumber(i): # Вызов функии для проверки ввода, ввел пользователь число или нет
                            i = float(i)
                            averg.append(i)
                        else:
                            print("\nВы ввели не число {}. Попробуйте снова\n".format(i))
                            haserrors = True
                    if haserrors != True:
                        break
            res = function.summa(averg)
            print("\nВаша сумма чисел равно : ", "{:.2f}".format(res)) # Вывод результата с форматным выводом до сотых
            print("\nДля завершения программы введите ctrl+c или ctrl+z+Enter\n")
    except KeyboardInterrupt:
        print("\nЗавершение программы. До новых встреч!")
    except EOFError:
        print("\nЗавершение программы. До новых встреч!))")


# def summa(num_list): # Функция отвечающая за счет произведения чисел
#     sum_num = 0
#     for x in num_list:
#         sum_num = sum_num + x
#     return sum_num


# def isNumber(element): # Функция для проверки ввода пользователем числа числа с плавающей точкой
#     result = True
#     try:
#         float(element)
#     except ValueError:
#         result = False
#     finally:
#         return result