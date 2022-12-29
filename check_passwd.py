def check_passwd(passwd):
    """ Функция для проверки пароля. 
    
    Проверяет кол-во символов, наличие цифр, факт того что пароль состоит не только из цифр и содержания слова password.
    Принимает строку passwd.
    Возвращает булево значения: True - в случае прохождения проверки, False - в случае её провала.
    
    """
    if len(passwd)>=6 and [s for s in passwd if s in '1234567890'] and passwd.isdigit()==False and ("password" in passwd.lower())!=True:
        return True
    else:
        return False
result=check_passwd(input("Введите ваш пароль: "))# Проверка данного ввода выполняется в функции, блок try..except не требуется.
if result==True:
    print("Ваш пароль прошёл проверку !")
else:
    print("Ваш пароль не прошёл проверку !")