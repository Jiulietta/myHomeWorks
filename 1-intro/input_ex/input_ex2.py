#Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
#на экран максимум из трёх, минимум из трёх или среднеарифметич

number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
number_3 = int(input("Введите третее число: "))

print("Чтобы получить максимальное значение введите 'max', "
      "чтобы получить минимальное значение введите 'min', "
      "чтобы получить среднеарифметическое введите 'Enter' ")

condition = input("Вводите: ").strip()
if condition=='max':
    print(max(number_1, number_2, number_3))
elif condition=='min':
    print(min(number_1, number_2, number_3))
else:
    print((number_1 + number_2 + number_3)/3)
