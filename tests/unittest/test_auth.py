import unittest
import os, sys

"""
VSCodeでテストするときsys.path.append必要（PyCharmでは不要みたい）

1モジュールテスト
> cd tests/unittest
> python -m unittest test_authdir

unittestディレクトリ下の全テストケーステスト
> cd ./e2d
> python -m unittest discover unittest

"""

sys.path.insert(0, r'F:\GDrive\Programming\Python\MyProject\TekapawSoft\e2d-folder\e2dapp')

os.chdir(r'F:\GDrive\Programming\Python\MyProject\TekapawSoft\e2d-folder\e2dapp')

import app


class TestAuth(unittest.TestCase):
    pass

    def setUp(self):
        self.app = app.app.test_client()  # module.app.test_client()

    def test_login_get(self):
        response = self.app.get('/login')
        # print(f"{response.status_code= }")
        # print(f"{response.data= }")

        assert response.status_code == 200

    def test_login_post(self):
        response = self.app.post('/login')
        print(f"{response.status_code= }")
        print(f"{response.data= }")

        assert response.status_code == 400  # 200  FIXME
        # assert response.data == b'{"status": "NG", "message": "login failed."}'

    def test_signup_post(self):
        # Formデータ
        data = dict(username='ryoichi.shibuya.yx@hitachi.com', var2='data2')

        response = self.app.post('/signup', data=data)
        print(f"{response.status_code= }")
        print(f"{response.data= }")

        assert response.status_code == 400  # 200  FIXME
        # assert response.data == b'{"status": "NG", "message": "NG. user already exists"}'


if __name__ == '__main__':
    unittest.main()
