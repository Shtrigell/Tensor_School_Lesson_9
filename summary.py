def summary(*args):
    """ Функция суммы.
    
    Функция для расчёта суммы чисел.
    Принимает неограниченное количество целочисленных значений - args.
    Возвращает целочисленное значение (сумму) - summ.
    
    """
    args_ch=[*args]
    for i in range (len(args)):
        try:
            args_ch[i] = int(args_ch[i])
        except ValueError:
            print("Неверный формат данных, данные будут удалены.")
            args_ch[i] = 0
    summ = 0
    for num in args_ch:
        summ += num
    return summ
print(summary(["aboba",1,2]))
