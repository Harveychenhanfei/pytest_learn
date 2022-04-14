import pytest

@pytest.mark.parametrize('username',['dongdong','xixi','beibei'])
@pytest.mark.parametrize('password',['p1','p2','p3'])
#多参数为字符串时,交替取值
def test_login(username,password):
    print('登录成功,用户名为{},密码为{}'.format(username,password))

if __name__ == '__main__':
    pytest.main(['-s','-v','multiparam_pytest.py'])