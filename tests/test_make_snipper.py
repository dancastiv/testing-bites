from lib.make_snippet import *

# test that it returns the first 5 words plus ellipses of a long string

def test_long_string_snippetted():
    snippet = make_snippet('Once upon a midnight dreary while I pondered weak and weary')
    assert snippet == 'Once upon a midnight dreary...'

# if it's 5 words or shorter we don't need to truncate

def test_short_string_not_snippetted():
    snippet = make_snippet('I am very short')

    assert snippet == 'I am very short'
    snippet2 = make_snippet('I am very short, sorry')
    assert snippet2 == 'I am very short, sorry'