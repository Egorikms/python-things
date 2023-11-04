import time
print("  Команды:")
print("")
print("  Слова - подсчёт слов")
print("  Пробелы - подсчёт пробелов")
print("  Символы - подсчёт символов")
print("  Знак - найти искомый знак")

time.sleep(5)

print("\nКоманда:")
deystvie = input()
print("Введите текст:")
text = input()

a = text.split()

if deystvie == "Слова":
    print("В тексте", len(a), "слов")

if deystvie == "Пробелы":
    print("В тексте", len(a)-1, "пробелов")

if deystvie == "Символы":
    print("В тексте", len(text), "Символов")

if deystvie == "Знак":
    znak = input("Введите искомый знак:")
    print("В тексте встретилось", text.count(znak), znak)

else:
    print("Введена недопустимая команда(")