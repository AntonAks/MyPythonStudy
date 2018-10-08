import win32serviceutil
import win32service
import win32event
import servicemanager


class AppServerSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "Python Test Service"
    _svc_display_name_ = "Python Test Service"
    _svc_description_ = "This is a test python service for UAT server. It will handle "

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.hWaitResume = win32event.CreateEvent(None, 0, 0, None)
        self.timeout = 10000  # Pause between execute of main service loop
        self.resumeTimeout = 1000
        self._paused = False

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STOPPED,
                              (self._svc_name_, ''))

    def SvcPause(self):
        self.ReportServiceStatus(win32service.SERVICE_PAUSE_PENDING)
        self._paused = True
        self.ReportServiceStatus(win32service.SERVICE_PAUSED)
        servicemanager.LogInfoMsg("The %s service has paused." % (self._svc_name_,))

    def SvcContinue(self):
        self.ReportServiceStatus(win32service.SERVICE_CONTINUE_PENDING)
        win32event.SetEvent(self.hWaitResume)
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        servicemanager.LogInfoMsg("The %s service has resumed." % (self._svc_name_,))

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    # Realisation of service
    def main(self):
        # Actions which need run when service will start
        servicemanager.LogInfoMsg("Python service is started")
        while True:
            # MAIN SERVICE CODE
            servicemanager.LogInfoMsg("I'm still here.")

            # Проверяем не поступила ли команда завершения работы службы
            # Checking for 'end service' command
            rc = win32event.WaitForSingleObject(self.hWaitStop, self.timeout)
            if rc == win32event.WAIT_OBJECT_0:
                # Actions which need run when service will stop
                servicemanager.LogInfoMsg("Service stopped !")
                break

                # Actions which need run when service will pause
            if self._paused:
                servicemanager.LogInfoMsg("Service on pause")
            # Pause service
            while self._paused:
                # Проверям не поступила ли команда возобновления работы службы
                # Checking for 'continue service' command
                rc = win32event.WaitForSingleObject(self.hWaitResume, self.resumeTimeout)
                if rc == win32event.WAIT_OBJECT_0:
                    self._paused = False
                    # Здесь выполняем необходимые действия при возобновлении работы службы
                    # Actions which need run when service will continue
                    servicemanager.LogInfoMsg("Service work is continued")
                    break


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(AppServerSvc)
