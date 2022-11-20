#Создать функцию, которую можно назвать как угодно Все что должна делать функция это определенный вывод
#Функция должна принимать определенный параметр в зависимости от которого будет немного изменяться вывод

#ps Можно с собственным макетом текста, только чтобы смена параметра влияла хотя бы на пару слов в выводе текста

#Пример работы функции:
#create_quote('yesterday')
#В консоли должно отобразиться:
#yesterday
#All my troubles seemed so far away,
#Now it looks as though they're here to stay.
#Oh, I believe in yesterday.

#Пример работы функции:
#create_quote('Вчера')
#В консоли должно отобразиться:
#Вчера
#All my troubles seemed so far away,
#Now it looks as though they're here to stay.
#Oh, I believe in Вчера.


name_of_cartoon = input()
def cartoons (name_of_cartoon):
#   print(f"{name_of_cartoon} - известный детский мультфильм. Дети обожают мультфильм {name_of_cartoon} за весёлый и интересный сюжет.")
cartoons(name_of_cartoon)
    return(f"{name_of_cartoon} - известный детский мультфильм. Дети обожают мультфильм {name_of_cartoon} за весёлый и интересный сюжет.")
cartoons(name_of_cartoon)