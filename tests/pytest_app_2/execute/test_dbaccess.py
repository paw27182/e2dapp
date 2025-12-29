"""
"pytest_app"を改良してみる

> cd ./tests/pytes_app_2/execute
> pytest -v -s test_dbaccess.py::TestDBAccess
> pytest -v test_dbaccess.py::TestDBAccess

Update: March 22, 2022
"""
import pytest
from pathlib import Path
from flask import Flask
from execute.dbaccess import DBAccess

app = Flask(__name__)

db_f = None  # define global variable


class TestDBAccess:
    def test_initialize(self, sqlite3_db):  # sqlite3_db: @pytest_fixture() 何もしていない（なくてもよい）
        """comment."""
        global db_f
        dbname = "db_guest"
        # tablename = "AIHUB申請書"
        tablename = "wine"

        with app.app_context():
            app.config.from_object("settings")  # public information
            app.config.from_pyfile(Path("instance", "config", "development.py"), silent=True)

            db_f = DBAccess(dbname, tablename)#, key, key_type)
            print(f"\n{db_f= }")

    def test_get_form_size(self, sqlite3_db):
        """comment."""
        global db_f
        tablename = "wine"
        selected_form = tablename
        form_size = db_f.get_form_size(selected_form)

        assert form_size == 178

    def test_read_form_items(self, sqlite3_db):
        """comment."""
        print('\nHello')
        assert (1, 2, 3) == (1, 2, 3)
