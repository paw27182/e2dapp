from pymongo import MongoClient
import pandas as pd
from datetime import datetime as dt

ftime = "%Y/%m/%d %H:%M:%S"


class AirQualityMongoDB:
    def __init__(self, database_name, host, accessid, accesspwd, collection_name):
        client = MongoClient(host, 27017)
        db = client[database_name]
        client[database_name].authenticate(accessid, accesspwd)

        self.collection = db[collection_name]

    def add(self, base_dir):
        data_file = base_dir + "/e2d/tests/airquality/AirQualityUCI-modified.csv"
        df = pd.read_csv(data_file)

        limit = int(df.shape[0] // 10 * 10)
        print(f"{limit= }")

        idx = self.collection.count_documents(filter={})
        print(f"{idx= }")

        if idx >= limit:
            self.collection.drop()

        records = df.iloc[idx:idx + 10].values  # pandas -> numpy
        values = [[record[0] + " " + record[1], *record[2:]] for record in records]

        key = ["Date", "CO_GT", "PT08_S1_CO", "C6H6_GT", "PT08_S2_NMHC",
               "NOx_GT", "PT08_S3_NOx", "NO2_GT", "PT08_S4_NO2", "PT08_S5_O3", "T", "RH", "AH", "up_date", "modified_by"]

        update_time = dt.now().strftime(ftime)
        modified_by = "guest@hitachi.com"

        rows = list()
        for row in values:  # values: list [[],[], ...]
            row.append(update_time)  # add timestamp
            row.append(modified_by)

            kv = {}
            for j, k in enumerate(key):
                kv[k] = row[j]

            rows.append(kv)
        self.collection.insert_many(rows)

        count = self.collection.count_documents(filter={})
        print(f"{count= }")


if __name__ == "__main__":
    base_dir = r"F:/OneDrive - Hitachi Group/Programming/Python/MyProject/TekapawSoft"
    # base_dir = r"D:/app"

    database_name = "db_guests"
    host = "localhost"
    accessid = "user1"
    accesspwd = "user1"
    collection_name = "airquality"
    aqm = AirQualityMongoDB(database_name, host, accessid, accesspwd, collection_name)
    aqm.add(base_dir)
