from transliterate import translit 

yazik = input("Выберите конечный язык(en, ru): ")
text = input("Введите текст: ")

if yazik == "en":
    text_ru = translit(text, language_code='ru', reversed=True)

elif yazik == "ru":
    text_ru = translit(text, 'ru')

else:
    print("Чтото не то...")

print(text_ru)

