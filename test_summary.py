import summary

def test_string_sum():
    """Тест на подачу функции строки и внутренную обработку ошибки

    Вернёт 0, если верно обратано ValueError. Tест вернёт True, если ошибка не обработана тест ляжет.
    Пишем обработку ValueError для прохождения теста.

    """
    assert summary.summary(["string","biba"])==0
    assert summary.summary(["string",5,5])==10
def test_string_succes():
    assert summary.summary([1,2,5])==8

