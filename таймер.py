import time

print("Минуты/секунды:")
tip_vremeni = input()

print ("О чём напомнить:")
text = (input())

if tip_vremeni == "Секунды":
    print ("Скока ждём:")
    vremya = float(input())
    time.sleep(vremya)
    print ("Время вышло!")
    print ("Напоминаю о:" + text)

if tip_vremeni == "Минуты":
    print ("Скока ждём:")
    vremya = float(input())
    a = vremya * 60
    time.sleep(a)
    print ("Время вышло!")
    print ("Напоминаю о:" + text)
