from lib.gratitudes import *

def test_Gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add('my dog')
    gratitudes.add('tea')
    formatted = gratitudes.format()
    assert formatted == 'Be grateful for: my dog, tea'

def test_no_Gratitudes():
    gratitudes = Gratitudes()
    formatted = gratitudes.format()
    assert formatted == 'Be grateful for: '