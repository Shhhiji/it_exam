import function

if __name__ == '__main__':
    try:
        while True:
            strok = input('Введите строку : ')
            num = input('Введите кол-во сколько раз повторить строку : ')
            num, error_str = function.oknum(num) # Возврат кортежа с проверкой что ввел пользователь
            if error_str is not None:
                print(error_str)
                continue
            if not function.isNumberint(num):
                error_str = 'Вы ввели не целое число {} . Попробуйте снова!\n'.format(num)
            function.povtor(num, strok)
    except KeyboardInterrupt:
        print('Завершение работы программы.')
    except EOFError:
        print('Завершение работы программы. Пока')    
        


# def povtor(num, strok):
#     for i in range(num):
#         print(strok)

# def oknum(num:str): # Проверка что ввел пользователь число или строку
#     number = None
#     error_str = None
#     if not isNumber(num):
#         error_str = '\nВы ввели не числовое значение {}. Попробуйте снова\n'.format(num)
#     elif not isNumberint(num):
#         error_str = '\nВы ввели не целое значение {}. Попробуйте снова\n'.format(num)
#     else:
#         num = int(num)
#         if num <= 0:
#             error_str = 'Вы ввели число {} меньше нуля или равное нулю. Попробуйте снова!\n'.format(num)
#         else:
#             number = num
#     return number, error_str