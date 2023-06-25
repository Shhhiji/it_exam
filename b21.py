import math
import function

    

def calcResult(c):
    return math.sqrt(c**2 + 5)

while True:
    c = int(input("Введите c целое число : "))
    d = int(input("Введите d целое число : "))
    h = int(input("Введите h целое число : "))
    if function.isNumberint(c) and function.isNumberint(d) and function.isNumberint(h):
        if(h <= 0):
            print("h должно быть больше 0")
        elif( d< c):
            print("d должно быть больше или рано c")
        else:
            while (c <= d):
                y = calcResult(c)
                print("y = {}\tc = {}".format(round(y, 2), c))
                c = c+h
    else:
        "Введено одно или несколько ничисловых значений"