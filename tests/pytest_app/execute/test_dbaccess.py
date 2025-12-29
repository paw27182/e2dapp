"""
> cd ./tests/pytes_app/execute
> pytest -v -s test_dbaccess.py
> pytest -v -s --setup-show test_dbaccess.py     # setUp, tearDown表示
> pytest -v -s -l --setup-show test_dbaccess.py  # -l 失敗時にローカル変数表示

Update: March 16, 2022
"""
import pytest
from pathlib import Path
from flask import Flask
from execute.dbaccess import DBAccess

app = Flask(__name__)


def test_initialize(sqlite3_db):  # sqlite3_db: @pytest_fixture()
    """comment."""
    dbname = "db_guest"
    # tablename = "AIHUB申請書"
    tablename = "wine"

    with app.app_context():
        app.config.from_object("settings")  # public information
        app.config.from_pyfile(Path("instance", "config", "development.py"), silent=True)

        db_f = DBAccess(dbname, tablename)#, key, key_type)
        print(f"\n{db_f= }")


def test_get_form_size(sqlite3_db):
    """comment."""
    dbname = "db_guest"
    # tablename = "AIHUB申請書"
    tablename = "wine"

    with app.app_context():
        app.config.from_object("settings")  # public information
        app.config.from_pyfile(Path("instance", "config", "development.py"), silent=True)

        db_f = DBAccess(dbname, tablename)#, key, key_type)
        print(f"\n{db_f= }")

    selected_form = tablename
    form_size = db_f.get_form_size(selected_form)

    assert form_size == 178


def test_read_form_items(sqlite3_db):
    """comment."""
    print('\nHello')
    assert (1, 2, 3) == (1, 2, 3)
