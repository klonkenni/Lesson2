#Практика: Сравнение строк


def check(val1, val2):
    if not isinstance(val1, str) or not isinstance(val2, str):
        return 0
    # Если строки одинаковые
    elif val1 == val2:
        return 1
    # Если строки разные и 2 строка это learn
    elif val2 != val1 and val2 == 'learn':
        return 3
    # Если строки разные и 1 строка длиннее.
    elif val1 != val2 and len(val1) > len(val2):
        return 2



print(check(15, '1')) #return 0
print(check('15', '15')) #return 1
print(check('15', '9')) #return 2
print(check('15', 'learn')) #return 3
print(check('learn444', 'learn')) #return 3

