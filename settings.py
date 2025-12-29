"""
1.submit and inquiry
"submit" flow (Navigation TAB: Entry - Submit a form)
    -> appmain/static/html/submit.html
    -> appmain/static/js/appmain.js
    -> appmain/appmain_bp.py
    -> render_template('area4Submit.html')

"inquire" flow (Navigation TAB: Inquire - Get a list of forms)
    -> appmain/static/html/inquire.html
    -> appmain/static/js/appmain.js
    -> appmain/static/appmain_bp.py
    -> render_template('area4Inquire.html')

2.Virtual Organization(login users)
Database administrators
  kate.walsh@example.com, mack.davis@example.com
Group administrators
  group_dx: sakura.suwa@example.com
  group_hr: goro.tani@example.com
  group_sales: harold.meachum@example.com

Update: December 28th, 2025
"""
from pathlib import Path

ENVIRONMENT = "development"
# ENVIRONMENT = "production"

BASE_DIR = Path(__file__).resolve().parent

# # In case of Windows 10/11
# PYTHON_EXE_FILE = r"C:/Python/env/Scripts/python.exe"  # specify python executable file
# HOST = "127.0.0.1"  # localhost
# PORT = 8000
# DB_ADMINISTRATOR = ["kate.walsh@example.com", "mack.davis@example.com"]
# DATABASE_TYPE = "SQLite3"
# # DATABASE_TYPE = "PostgreSQL"  # UNDISCLOSED
# # DATABASE_TYPE = "MongoDB"  # UNDISCLOSED

# # In case of Ubuntu 20.04.6 LT
# # PYTHON_EXE_FILE = "/home/paw/enve2d/bin/python3.11"  # specify python executable file
# PYTHON_EXE_FILE = "/home/paw/env/bin/python3.11"  # specify python executable file
# HOST = "127.0.0.1"
# PORT = 8000
# DB_ADMINISTRATOR = ["kate.walsh@example.com", "mack.davis@example.com"]
# DATABASE_TYPE = "SQLite3"

# In case of Azure(Linux)
HOST = None
PORT = None
DB_ADMINISTRATOR = ["kate.walsh@example.com", "mack.davis@example.com"]
DATABASE_TYPE = "SQLite3"
