# Задание - обрабатывать исключение, если ввел некорректные данные
def get_summ(num_one, num_two):
    try:
        result = int(num_one) + int(num_two)
        print("Сумма чисел:" + str(result))
    except ValueError:
        print("Вы ввели некорректные данные. Введите числа")


get_summ(1, "аа")
