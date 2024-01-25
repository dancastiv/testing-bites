from lib.greet import *

def test_greet_danny():
    greeting = greet('Danny')
    assert greeting == 'Hello, Danny!'

def test_greet_dr_lecter():
    greeting = greet('Dr. Lecter')
    assert greeting == 'Hello, Dr. Lecter!'