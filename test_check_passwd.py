import check_passwd

def test_len():
    assert check_passwd.check_passwd("5букв")==False

def test_in_numbers():
    assert check_passwd.check_passwd("nonumbers")==False

def test_only_numers():
    assert check_passwd.check_passwd("1234567890")==False

def test_password_word():
    assert check_passwd.check_passwd("PaSSwOrd")==False

def test_succeful():
    assert check_passwd.check_passwd("Am0gu$23")==True