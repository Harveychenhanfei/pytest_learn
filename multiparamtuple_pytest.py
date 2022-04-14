import pytest

@pytest.mark.parametrize('username,password',[('dongdong','pd'),('xixi','px')])
def test_register(username,password):
    print('登录成功,用户名为{},密码为{}'.format(username,password))

if __name__ == '__main__':
    pytest.main(['-s','-v','multiparamtuple_pytest.py'])