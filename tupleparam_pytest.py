import pytest

@pytest.mark.parametrize('userId',[(1,2),(3,4)])
def test_login(userId):
    print('登录成功,登录id为{}'.format(userId))

if __name__ == '__main__':
    pytest.main(['-s','-v','tupleparam_pytest.py'])