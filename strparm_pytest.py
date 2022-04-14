import pytest

@pytest.mark.parametrize('username',['doongdong','xixi','beibei']) #参数化
def test_login(username):
    print('登录成功,用户名为%s'%username)

if __name__ == '__main__':
    pytest.main(['-s','-v','strparm_pytest.py'])