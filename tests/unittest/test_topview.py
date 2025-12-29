import unittest

import sys
# sys.path.insert(0, 'F:\OneDrive - Hitachi Group\Programming\Python\MyProject\TekapawSoft\e2d')
sys.path.insert(0, r'H:\その他のパソコン\My Laptop\GDrive\Programming\Python\MyProject\TekapawSoft\e2d-folder\e2dapp')

import app


class TestTopview(unittest.TestCase):

    def setUp(self):
        with app.app.test_client() as c:  # module.app.test_client()
            with c.session_transaction() as sess:
                sess['user'] = 'ryoichi.shibuya.yx@hitachi.com'  # sessionオブジェクトのデータ
        self.app = c

    def test_topview_get(self):
        # Formデータ
        data = dict(user='ryoichi.shibuya.yx@hitachi.com', var2='data2')

        response = self.app.get('/topview', data=data)
        # print(f"{response.status_code= }")
        # print(f"{response.data= }")

        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
