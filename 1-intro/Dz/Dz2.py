# Пользователь вводит с клавиатуры число. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero

x = int(input("Введите число: "))
if x==0:
    stroka="Number is equal to zero"
else:
    stroka="Number is positive" if x>0    else "Number is negative"
print(stroka)