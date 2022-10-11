#todo: Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
чтобы каждая функция выполняла одно универсальное действие.

words = ["оператор", "конструкция", "объект"]
desc_ = ["Это слово обозначает наименьшую автономную часть языка программирования", "Это слово 2", "Это слово 3"]

mask = []


def init(desc_):  # функция случайным образом выбирает вопрос, выводит его на экран и возвращает номер вопроса
    import random
    question = random.randint(0, len(words) - 1)
    print(desc_[question])
    print("Слово состоит из", len(words[question]), "букв")
    print(
        "У вас есть 10 попыток. За неудачную попытку начисляется штрафной бал. Игра продолжается до 10 штрафных баллов")
    return question


question = init(desc)


def get_mask(question):  # функция задает шаблон и выводит определение слова по шаблону
    global mask
    for i in words[question]:
        mask.append("▒")  # выводим шаблон
    print(mask)


get_mask(question)

# количество угаданных букв
attempts = 10  # количество попыток
success = 0  # количество успешных попыток


def attempt_lost(attempt_count):  # функция начисления штрафных баллов
    return (attempt_count - 1)


def count_(answer):  # возвращает количество вхождений введной буквы в слово
    return words[question].count(answer)


def success_(answer):  # функция начисляет баллы за угаданные буквы. 1 балл = 1 угаданная буква
    global mask
    count = 0
    success = 0
    for i in words[question]:
        count = count + 1
        if i == answer:
            mask[count - 1] = i
    success = success + count_(answer)
    return success


while success < len(words[question]):  # выполняем цикл пока слово не будет угадно полностью
    if attempts == 0:
        break

    answer = input("Введите букву: ")

    if count_(answer) == 0:  # если введена неправильная буква
        attempts = attempt_lost(attempts)
        print("Вы ввели неверную букву, у вас осталось", attempts, "попыток")

    else:
        if answer not in mask:  # проверяем была ли введенная буква угадана ранее
            success_(answer)
            print(mask)
        else:  # если буква была угадана ранее уменьшаем количество оставшихся попыток
            attempts = attempt_lost(attempts)
            print("Такая буква уже открыта в слове. У вас осталось", attempts, "попыток")
            continue

    success = success + success_(answer)

if success == len(words[question]) and "▒" not in mask:
    print("Вы выйграли, поздравляю!")
else:
    print("Вы израсходовали 10 попыток. Удачи в следующий раз")