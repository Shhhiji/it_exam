import function

if __name__ == '__main__':
    try:
        while True: 
            res = function.str_list() # Возврат списка
            result = function.zamena(res) # Функция замены л на !!!!!
            print('\nВаш измененный текст : ')
            print(' ')
            for i in result:
                print(i, '\n')
    except KeyboardInterrupt:
        print('\n\n     Завершение работы программы.\n                  Пока')
        
        
# def str_list(): # Функция для ввода пользователем любого текста и выход из программы
#     exitStr = "\x1a" # hex код сочетания ctrl+z
#     list_ent = list()
#     try:
#         print('Замена букв в тексте пользователя.')
#         while True:
#             print('\nДля вывода результата нажмите ctrl+z+Еnter')
#             print('Для завершения работы программы нажмите ctrl+c')
#             ent = input('\nВведите ваше сообщение : ')
#             if ent.__contains__(exitStr): # проверка содержит ли строка crl+z 
#                 ent = ent.split(exitStr)[0]
#                 list_ent.append(ent)
#                 break
#             else:
#                 list_ent.append(ent)
#     except EOFError:
#         print('\nВывод результата...')
#     return list_ent

# import re

# def zamena(list_ent): # Функция для замены символов
#     ret = [] 
#     for i in list_ent:
#         i_n = re.sub("л|Л", "!!!!", i)
#         ret.append(i_n)
#     return ret

