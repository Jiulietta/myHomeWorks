# (Список №1) ~5 имен, среди которых должно быть ваше имя
#  Вывести в консоль ваше имя обратившись к нему через индекс в списке
#
#  (Список №2) из чисел наполнить его годами (годы например 1980) ~ 5 записей хватит
#
# (Список №3) который будет состоять из двух ранее объявленных списков
#  Вывести консоль обращаясь через этот список (Список №3) перевое имя указанное во вложенном списке с именами
#  и последний год указанный во вложенном списке с годами.

amici = ["Giulia", "Olessia", "Daniele", "Antonio", "Francesco"]
print(amici[0])

anni = [2008, 2009, 2010, 2011, 2012]

lavoro = [amici, anni]
print(lavoro[0][0], lavoro[1][-1])

