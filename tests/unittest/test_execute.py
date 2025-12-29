import unittest
from werkzeug.datastructures import FileStorage

# import sys
# sys.path.insert(0, 'F:\OneDrive - Hitachi Group\Programming\Python\MyProject\TekapawSoft\e2d')

import app


class TestExecute(unittest.TestCase):

    def setUp(self):
        with app.app.test_client() as c:  # module.app.test_client()
            with c.session_transaction() as sess:
                sess['user'] = 'ryoichi.shibuya.yx@hitachi.com'
        self.app = c

    def test_execute_post_get_a_list_of_forms(self):
        # Formデータ
        data = dict(command="get_a_list_of_forms")

        response = self.app.post('/execute', data=data)
        # print(f"{response.status_code= }")
        # print(f"{response.data= }")

        assert response.status_code == 200

    def test_execute_post_submit_a_form(self):
        # Excel帳票データ
        my_data = r"F:\OneDrive - Hitachi Group\Programming\Python\MyProject\TekapawSoft\e2d\tests\帳票サンプル_guests\AIHUB申請書.xlsx"
        my_file = FileStorage(
            stream=open(my_data, "rb"),
            filename="AIHUB申請書.xlsx",
            content_type="application/octet-stream",
        )

        # Formデータ
        data = dict(command="submit_a_form", data_file=my_file)

        response = self.app.post('/execute', data=data, content_type="multipart/form-data")
        # print(f"{response.status_code= }")
        # print(f"{response.data= }")

        assert response.status_code == 200

    def test_execute_post_statistics_analysis(self):
        data = dict(command="statistics_analysis",
                    selected_form="wine",
                    database_type="mongodb",
                    owner_group="group_guests",

                    # includeSqlite3Check="",
                    # record_to_be_processed="",
                    # executeParameters="",
                    # user='ryoichi.shibuya.yx@hitachi.com',
                    # var2='data2',
                    )

        response = self.app.post('/execute', data=data)
        # print(f"{response.status_code= }")
        # print(f"{response.data= }")

        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
