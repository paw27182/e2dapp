import pytest
import sys

sys.path.insert(0, r"F:\OneDrive - Hitachi Group\Programming\Python\MyProject\TekapawSoft\e2d-folder\app")
# print(f"{sys.path= }")


@pytest.fixture(scope="function")
def sqlite3_db(tmpdir):
    """comment."""
    # pre-processing
    print('\n***** pre-processing *****')

    yield

    # post-processing
    print('\n***** post-processing *****')
