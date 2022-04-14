import pytest

x = 1
y=0

str1='py'
str2='python'
str3 = 'java'
str4 = 'python'
def test_int_001():
    assert x

def test_int_002():
    assert not y

def test_int_003():
    assert str1 in str2

def test_int_004():
    assert str2 != str3

def test_int_005():
    assert str2 == str4


if __name__ == '__main__':
    pytest.main(['-s','-v','assert_pytest.py'])