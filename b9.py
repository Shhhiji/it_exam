import function

bot = -50
top = 50

if __name__ == '__main__':
    try:
        while True:
            print("Среднеарифметическое чисел больше 10. Для остановки работы программы нажмите ctrl+z+Enter или ctrl+c")
            n = input("\nВведите целое положительное число : ")
            if not function.isNumberint(n):  # проверка ввел ли пользователь число
                print('\nВы ввели не число, а строчное значение ({}) . Попробуйте снова!\n'.format(n))
                continue
            n = int(n)
            if n <= 0:
                print('\nВы ввели ({}) значение выходящее за диапозон генерируемых чисел.\nЧисло не может быть отрицательным или равным нулю!\nПопытайтесь снова!\n'.format(n))
                continue
            numbers, res = function.arifmetic(n, bot, top) # возврат кортежа из функции
            print('\nСписок ваших сгенерированных чисел в промежутке от [{};{}] : {}'.format(bot, top, numbers))
            print("Среднеарифметическое чисел больше 10 : ", "{:.2f}".format(res))
            print('')
    except KeyboardInterrupt:
        print('\nЗавершение работы программы.\nДо новых встреч! :)')
        print(' ')
    except EOFError:
        print('\nЗавершение работы программы.\nДо новых встреч!')
        print(' ') 

# def isNumberint(element): # Функция для проверки ввода пользователем целого числа
#     result = True
#     try:
#         int(element)
#     except ValueError:
#         result = False
#     finally:
#         return result


# def arifmetic(n, bot, top): # Генерируем рандомно числа из заданного промежутка и считаем среднеарифметическое чисел больше 10
#     numbers = []
#     pos = []
#     for i in range(n):
#         numbers.append(random.randint(bot, top))
#     for i in numbers:
#         if i >= 10:
#             pos.append(i)
#     summa = sum(pos)
#     leng = len(pos)
#     arif = summa/leng
#     return numbers, arif