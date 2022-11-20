#Пользователь вводит с клавиатуры числа.
#Если число больше нуля нужно вывести надпись «Number is positive»,
#если меньше нуля «Number is negative»,
#если равно нулю «Number is equal to zero».
#Когда пользователь вводит число 7 программа прекращает свою работу и выводит
#на экран надпись «Good bye!»


while True:
    try:
        a = int(input("Введите число: "))

    #a=int(input("Введите число: "))
        while a!=7:
            if a>0:
                print('The number is positive')
            elif a==0:
                print('The number is equal to zero')
            else:
                print('The number is negative')
            a=int(input("Введите число: "))
        try:
            a==7/0
        except ZeroDivisionError:
            print('Goodbye!')
            a=int(input("Введите число: "))
            if a>0:
                print('The number is positive')
            elif a==0:
                print('The number is equal to zero')
            else:
                print('The number is negative')

    except Exception:
        print("Вы ввели не число, повторите ввод: ")
