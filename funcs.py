def add():
    item = int(input("Введите первое число: "))
    summand = int(input("Введите второе число: "))
    result = item + summand
    return result


def diff():
    # инпуты двух числе для вычитания
    minuend = int(input("Введите уменьшаемое число: "))
    subtrahend = int(input("Введите вычитаемое: "))
    # разница
    diff = minuend - subtrahend
    return diff



if __name__ == '__main__':
    print("Сумма равна: ", add())
