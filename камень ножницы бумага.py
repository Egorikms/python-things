import random
import time 

i = 1

print("Камень Ножницы Бумага")
time.sleep(2.5)


chel = input("Ваш ход: ")
robot = ["Камень", "Ножницы", "Бумага"]

hod_robot = random.choice(robot)

if chel == "Ножницы" and hod_robot == "Бумага":
    print("Ход робота: " + hod_robot)
    time.sleep(2)
    print("Вы выиграли)")

elif chel == "Бумага" and hod_robot == "Камень":
    print("Ход робота: " + hod_robot)
    time.sleep(2)
    print("Вы выиграли)")

elif chel == "Камень" and hod_robot == "Ножницы":
    print("Ход робота: " + hod_robot)
    time.sleep(2)
    print("Вы выиграли)")

elif chel == "ножницы" and hod_robot == "Бумага":
    print("Ход робота: " + hod_robot)
    time.sleep(2)
    print("Вы выиграли)")

elif chel == "бумага" and hod_robot == "Камень":
    print("Ход робота: " + hod_robot)
    time.sleep(2)
    print("Вы выиграли)")

elif chel == "камень" and hod_robot == "Ножницы":
    print("Ход робота: " + hod_robot)
    time.sleep(2)
    print("Вы выиграли)")

elif chel == "Бумага" and hod_robot == "Ножницы":
    print("Ход робота: " + hod_robot)
    time.sleep(2)
    print("Вы проиграли(")

elif chel == "Камень" and hod_robot == "Бумага":
    print("Ход робота: " + hod_robot)
    time.sleep(2)
    print("Вы проиграли(")

elif chel == "Ножницы" and hod_robot == "Камень":
    print("Ход робота: " + hod_robot)
    time.sleep(2)
    print("Вы проиграли(")

elif chel == "бумага" and hod_robot == "Ножницы":
    print("Ход робота: " + hod_robot)
    time.sleep(2)
    print("Вы проиграли(")

elif chel == "камень" and hod_robot == "Бумага":
    print("Ход робота: " + hod_robot)
    time.sleep(2)
    print("Вы проиграли(")

elif chel == "ножницы" and hod_robot == "Камень":

    print("Ход робота: " + hod_robot)
    time.sleep(2)
    print("Вы проиграли(")

else:
    print("Вы ввели недопустипую команду...")

print("")