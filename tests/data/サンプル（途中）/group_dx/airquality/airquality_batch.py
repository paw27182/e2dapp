import time
import sqlite3
import pandas as pd

base_dir = r"F:/OneDrive - Hitachi Group/Programming/Python/MyProject/TekapawSoft"
# base_dir = r"D:/flaskapp"

dbname = base_dir + "/e2d/database/airquality.sqlite3"

data_file = base_dir + "/e2d/tests/airquality/AirQualityUCI-modified.csv"
df = pd.read_csv(data_file)

sql = "CREATE TABLE IF NOT EXISTS airquality " \
      "(Date text, CO_GT real, PT08_S1_CO real, C6H6_GT real, PT08_S2_NMHC real," \
      " NOx_GT real, PT08_S3_NOx real, NO2_GT real, PT08_S4_NO2 real, PT08_S5_O3 real," \
      " T real, RH real, AH real, PRIMARY KEY(Date));"
print("sql= ", sql)

with sqlite3.connect(dbname) as conn:
    conn.execute(sql)

sql = "INSERT INTO airquality " \
      "(Date, CO_GT, PT08_S1_CO, C6H6_GT, PT08_S2_NMHC," \
      " NOx_GT, PT08_S3_NOx, NO2_GT, PT08_S4_NO2, PT08_S5_O3," \
      " T, RH, AH) " \
      "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)"
print("sql= ", sql)

c = conn.execute('SELECT count(*) FROM airquality;')  # debug code
count1 = c.fetchone()
print(f"{count1= }")

while True:
    for i in range(0, int(df.shape[0] // 10 * 10), 10):
        records = df.iloc[i:i + 10].values  # pandas -> numpy
        values = [[record[0] + " " + record[1], *record[2:]] for record in records]

        try:
            with sqlite3.connect(dbname) as conn:
                conn.executemany(sql, values)
                conn.commit()
        except Exception as err:
            continue

        time.sleep(10)

        c = conn.execute('SELECT count(*) FROM airquality;')  # debug code
        count2 = c.fetchone()
        print(f"{count2= }")

    #         break  # debug code

    conn.execute('DELETE FROM airquality;')
    conn.commit()
