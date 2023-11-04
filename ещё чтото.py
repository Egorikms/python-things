print("\nВедите текст:")

text = input()

a1 = text.split()

a = len(text)
b = len(text.split())
c = b - 1

print(a, "символов")
print(b, "слов")
print(c, "пробелов")