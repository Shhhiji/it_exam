import function

bot = -50
top = 50

if __name__ == '__main__':
    try:
        while True:
            print("Максимальное значение. Для остановки работы программы нажмите ctrl+z+Enter или ctrl+c")
            n = input("\nВведите целое положительное число : ")
            if not function.isNumberint(n):  # проверка ввел ли пользователь число
                print('\nВы ввели не число, а строчное значение ({}) . Попробуйте снова!\n'.format(n))
                continue
            n = int(n)
            if n <= 0:
                print('\nВы ввели ({}) значение выходящее за диапозон генерируемых чисел.\nЧисло не может быть отрицательным или равным нулю!\nПопытайтесь снова!\n'.format(n))
                continue
            numbers, res = function.max_num(n, bot, top) # возврат кортежа из функции
            print('\nСписок ваших сгенерированных чисел в промежутке от [{};{}] : {}'.format(bot, top, numbers))
            print("Максимальное значение : ", "{:.2f}".format(res))
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

# def max_num(n, bot, top): # Генерируем рандомно числа из заданного промежутка и ищем мах число
#     numbers = []
#     for i in range(n):
#         numbers.append(random.randint(bot, top))
#     res = max(numbers)
#     return numbers, res