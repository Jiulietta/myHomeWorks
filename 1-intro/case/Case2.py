#Пользователь вводит с клавиатуры три числа. Первое
#число — зарплата за месяц, второе число — сумма месячного платежа по кредиту в банке, третье число — задолженность за коммунальные услуги.
# Необходимо вывести на экран сумму, которая останется у пользователя после всех выплат.

a = float(input("Введите зарплату за месяц: "))
b = float(input("Введите сумму месячного платежа по кредиту в банке: "))
c = float(input("Введите задолженность за коммунальные услуги: "))

print("Оставшаяся после выплат сумма:")
res = (a-b-c)
print(res)