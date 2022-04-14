import pytest

def test_login():
    print('test_login会被执行')

def testLogin():
    print('testLogin会被执行')

def logintest():
    print('logintest不会被执行')

def login_test():
    print('login_test不会被执行')

if __name__ == '__main__':
    pytest.main(['-v','-s','test_pytest.py'])