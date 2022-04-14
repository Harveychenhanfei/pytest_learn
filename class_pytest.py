import pytest
class TestOrdering():

    def test_login(self):
        print('正在登录')
        assert 0

    def test_add(self):
        print('正在增加')

    def test_del(self):
        print('正在删除')

    def not_test(self):
        print('不以test开头的')

if __name__ == '__main__':
    pytest.main(['-s','-v','class_pytest.py'])