import os
import win32service 
import win32serviceutil 
import win32event 
import datetime 
from airquality_sqlite3 import AirQualitySqlite3
from airquality_mongodb import AirQualityMongoDB


class SmallestPythonService(win32serviceutil.ServiceFramework): 
    # サービス名 
    _svc_name_ = "WinService"
    # サービス画面表示名
    _svc_display_name_ = "Win Service" 
    # サービス説明
    _svc_description_ = '一定周期でデータをテーブルに保存する'
    # イベントシグナル待ち時間
    # _timeout_Milliseconds = 3_000    #   3秒
    # _timeout_Milliseconds = 10_000   #  10秒
    _timeout_Milliseconds = 300_000  # 300秒（5分）

    def __init__(self, args): 
        win32serviceutil.ServiceFramework.__init__(self, args) 
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None) 

    def SvcStop(self): 
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING) 
        win32event.SetEvent(self.hWaitStop) 

    def SvcDoRun(self): 
        print('サービス開始') 
        while 1:
            # イベントシグナル待ち（10秒）
            ret = win32event.WaitForSingleObject(
                    self.hWaitStop,
                    self._timeout_Milliseconds
                    )
            # サービス停止(イベントがシグナル化)ならば、処理を中止
            if ret == win32event.WAIT_OBJECT_0:
                break

            self.main_loop()

    # サービス処理
    def main_loop(self): 

        # print('サービス開始')
        # # ↓↓ test用のため削除　実行ディレクトリにtest.txt作成されたらテストOK
        # FILEADDR = os.path.dirname(os.path.abspath(__file__)) + '/test.txt'
        # with open(FILEADDR, "a") as f:
        #     f.write("[Test] %s \n" % (datetime.datetime.now()))

        base_dir = r"F:/OneDrive - Hitachi Group/Programming/Python/MyProject/TekapawSoft"
        # base_dir = r"D:/app"

        # sqlite3
        aq = AirQualitySqlite3(base_dir)
        aq.add()

        # mongodb
        aqm = AirQualityMongoDB("db_guests", "localhost", "user1", "user1", "airquality")
        aqm.add(base_dir)


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(SmallestPythonService) 
