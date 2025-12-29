import sqlite3
import pandas as pd
from datetime import datetime as dt

ftime = "%Y/%m/%d %H:%M:%S"


class AirQualitySqlite3:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.dbname = base_dir + "/e2d/database/db_guests.sqlite3"

        sql = "CREATE TABLE IF NOT EXISTS airquality " \
              "(Date text, CO_GT real, PT08_S1_CO real, C6H6_GT real, PT08_S2_NMHC real," \
              " NOx_GT real, PT08_S3_NOx real, NO2_GT real, PT08_S4_NO2 real, PT08_S5_O3 real," \
              " T real, target real, AH real, up_date text, modified_by text, PRIMARY KEY(Date));"
        print("sql= ", sql)

        with sqlite3.connect(self.dbname) as conn:
            conn.execute(sql)

    def add(self):
        data_file = self.base_dir + "/e2d/tests/airquality/AirQualityUCI-modified.csv"
        df = pd.read_csv(data_file)

        limit = int(df.shape[0] // 10 * 10)
        print(f"{limit= }")

        with sqlite3.connect(self.dbname) as conn:
            c = conn.execute('SELECT count(*) FROM airquality;')  # debug code
            idx = c.fetchone()[0]
            print(f"{idx= }")

        if idx >= limit:
            with sqlite3.connect(self.dbname) as conn:
                conn.execute('DELETE FROM airquality;')
                conn.commit()

        update_time = dt.now().strftime(ftime)
        modified_by = "guest@hitachi.com"

        records = df.iloc[idx:idx + 10].values  # pandas -> numpy
        values = [[record[0] + " " + record[1], *record[2:], update_time, modified_by] for record in records]

        sql = "INSERT INTO airquality " \
              "(Date, CO_GT, PT08_S1_CO, C6H6_GT, PT08_S2_NMHC," \
              " NOx_GT, PT08_S3_NOx, NO2_GT, PT08_S4_NO2, PT08_S5_O3," \
              " T, target, AH, up_date, modified_by) " \
              "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        print("sql= ", sql)

        with sqlite3.connect(self.dbname) as conn:
            conn.executemany(sql, values)
            conn.commit()

        c = conn.execute('SELECT count(*) FROM airquality;')  # debug code
        count = c.fetchone()
        print(f"{count= }")


if __name__ == "__main__":
    base_dir = r"F:/OneDrive - Hitachi Group/Programming/Python/MyProject/TekapawSoft"
    # base_dir = r"D:/app"

    aq = AirQualitySqlite3(base_dir)
    aq.add()
