import pytest

def setup_module():
    print("这是测试用例的前置module")

def teardown_module():
    print("则是测试用例的后置module")

def test_01():
    print("用例01")
def test_02():
    print("用例02")

if __name__ == '__main__':
    pytest.main(['-v','-s','module_pytest.py'])