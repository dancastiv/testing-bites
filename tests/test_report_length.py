from lib.report_length import *

def test_short_string():
    length = report_length('yo')
    assert length == 'This string was 2 characters long.'

def test_long_string():
    length = report_length('spectacularly')
    assert length == 'This string was 13 characters long.'

def test_empty_string():
    length = report_length('')
    assert length == 'This string was 0 characters long.'