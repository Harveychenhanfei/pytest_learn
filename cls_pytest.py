import pytest

class Test():

    def setup_class(self):
        print("这是测试用例前置")

    def teardown_class(self):
        print("这是测试用例后置")

    def test_01(self):
        print("用例1")

    def test_02(self):
        print("用例2")


if __name__ == '__main__':
    pytest.main(['-v','-s','cls_pytest.py'])