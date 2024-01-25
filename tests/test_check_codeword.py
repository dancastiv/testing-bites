from lib.check_codeword import *

def test_correct_codeword():
    check = check_codeword('horse')
    assert check == 'Correct! Come in.'

def test_close_codeword():
    check = check_codeword('hearse')
    assert check == 'Close, but nope.'

def test_wrong_codeword():
    check = check_codeword('meow')
    assert check == 'WRONG!'