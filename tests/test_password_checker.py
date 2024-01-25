from lib.password_checker import *
import pytest

# check we get True if the password is >= 8 characters long

def test_password_is_valid():
    password = PasswordChecker()
    checked_password = password.check('superpassword')

    assert checked_password == True

# check for an Exception if the password is < 8 characters long

def test_password_is_short():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check('hi')
    error_message = str(e.value)
    assert error_message == 'Invalid password, must be 8+ characters.'

# empty passwords also shouldn't work
    
def test_no_password():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check('')
    error_message = str(e.value)
    assert error_message == 'Invalid password, must be 8+ characters.'