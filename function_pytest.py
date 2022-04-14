import pytest

def setup_function():
    print("这是用例前置")

def teardown_function():
    print("这是用例后置")

def test_01():
    print("用例01")

def test_02():
    print("用例02")


if __name__ == '__main__':
    pytest.main(['-v','-s','function_pytest.py'])