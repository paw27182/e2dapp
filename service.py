import os
import sys
sys.path.append("C:\Python\env\Lib\site-packages")  # 2022.1.18
sys.path.append("C:\Python\env\Lib\site-packages\win32\lib")  # 2022.1.18

import win32serviceutil
import win32service
import win32event
import win32evtlogutil
import servicemanager
import socket
import logging
import time
import pathlib

from waitress import serve  # 2022.1.18

sys.stdout = sys.stderr = open(os.devnull, 'w')  # fix code 2021.6.17

sys.path.append(os.path.dirname(__name__))
# from myapp import app
from app import app


logging.basicConfig(
    # filename=r'c:\temp\winservice\flask_service\hello-service.log',
    # filename=r'C:\Users\fibo2\OneDrive - Hitachi Group\Programming\Python\MyProject\Language\miscellaneous\winservice\flask_service\hello-service.log',
    filename=pathlib.Path(pathlib.Path().resolve(__file__), "hello-service.log"),
    level=logging.DEBUG,
    format='[helloflask] %(levelname)-7.7s %(message)s'
)


class HelloFlaskSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "FlaskService"
    _svc_display_name_ = "Flask Service"
    
    def __init__(self, *args):
        win32serviceutil.ServiceFramework.__init__(self, *args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(5)
        self.stop_requested = False

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)
        logging.info('Stopped service ...')
        self.stop_requested = True

    def SvcDoRun(self):
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, '')
        )

        self.main()

    def main(self):
        # app.run(host="127.0.0.1", port=8000)
        serve(app, host='127.0.0.1', port=5002, threads=10)  # FlaskアプリをWaitressで稼働させる 2022.1.18

        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, __name__)
        )
        
        # # debug code
        # while 1:
        #     servicemanager.LogMsg(
        #         servicemanager.EVENTLOG_INFORMATION_TYPE,
        #         servicemanager.PYS_SERVICE_STARTED,
        #         (self._svc_name_, '+++++')
        #     )
        #     time.sleep(10)


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(HelloFlaskSvc)
