def add():
    print("Сейчас будем складывать два числа")
    item = int(input("Введите первое число: "))
    summand = int(input("Введите второе число: "))
    result = item + summand
    return result


def diff():
    print("Сейчас будем вычитать два числа")
    minuend = int(input("Введите уменьшаемое число: "))
    subtrahend = int(input("Введите вычитаемое: "))
    # разница
    diff = minuend - subtrahend
    return diff



if __name__ == '__main__':
    print("Сумма равна: ", add())
