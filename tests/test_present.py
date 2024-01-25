from lib.present import *
import pytest

# test for being able to unwrap a thing we wrapped (expected behaviour)

def test_wrap_and_unwrap():
    present = Present()
    present.wrap('hello')
    contents = present.unwrap()
    assert contents == 'hello'

#unwrapping before wrapping shouldn't work and should return an error message

def test_unwrap_before_wrap():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == 'No contents have been wrapped.'

#wrapping more than once should return error message
    
def test_wrap_and_rewrap():
    present = Present()
    present.wrap('what')
    with pytest.raises(Exception) as e:
        present.wrap('ever')
    error_message = str(e.value)
    assert error_message == 'A contents has already been wrapped.'

