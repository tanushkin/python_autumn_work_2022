#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
#Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
# Данную задачу нужно решить с помощью конструкции  match  (Python v3.10)


# Пример:
# Введите единицу массы тела
#       1 - килограмм
#       2 — миллиграмм
#       3 — грамм
#       4 — тонна
#       5 — центнер
#>4

#Введите  массу тела
#>1

#Ответ: 1000 кг

def Введите_единицу_массы_тела (T):
    match T:
        case "1":
            print("килограмм")
        case "2":
            print("милиграмм")
        case "3":
            print("грамм")
        case "4":
            print("тонна")
        case "5":
            print("центов")

M = int(1000)
print(M), Введите_единицу_массы_тела("1")
