a = float(input("Введи первое число:"))
uwu = input("Действие:")
b = float(input("Введи второе число:"))

if uwu == "+":
    c = a + b
    print("Результат:" + str(c))
elif uwu == "-":
    c = a - b
    print("Результат:" + str(c))
elif uwu == "/":
    c = a / b
    print("Результат:" + str(c))
elif uwu == "*":
    c = a * b
    print("Результат:" + str(c))
else:
    print("Результат: " + "Что-то не так(")
