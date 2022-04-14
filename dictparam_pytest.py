import pytest

@pytest.mark.parametrize('register',[{'name':'dongdong'},{'password':123456}])
def test_register(register):
    print('注册成功,注册信息为{}'.format(register))

if __name__ == '__main__':
    pytest.main(['-s','-v','dictparam_pytest.py'])