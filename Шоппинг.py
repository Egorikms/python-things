import time

tovar1 = 700
tovar2 = 1000
tovar3 = 250
tovar4 = 55
tovar5 = 190

print ("\nПрайс:")
print (f"Товар 1 - {tovar1}руб/шт")
print (f"Товар 2 - {tovar2}руб/шт")
print (f"Товар 3 - {tovar3}руб/шт")
print (f"Товар 4 - {tovar4}руб/шт")
print (f"Товар 5 - {tovar5}руб/шт")

time.sleep(5)

rub_tovar1 = int(input("\nСколько берём Товар 1:"))
rub_tovar2 = int(input("Сколько берём Товар 2:"))
rub_tovar3 = int(input("Сколько берём Товар 3:"))
rub_tovar4 = int(input("Сколько берём Товар 4:"))
rub_tovar5 = int(input("Сколько берём Товар 5:"))

a = rub_tovar1 * tovar1
b = rub_tovar2 * tovar2
c = rub_tovar3 * tovar3
d = rub_tovar4 * tovar4
e = rub_tovar5 * tovar5

cena = a + b + c + d + e

print (f"\nИтого: {cena}руб")
print ("Спасибо за покупку!")