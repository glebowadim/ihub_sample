import time

from onevizion import IntegrationLog, LogLevel


class Integration:

    def __init__(self, url: str, user_name: str, password: str, process_id: int, log_level_name: str):
        url = url.replace("https://", "").replace("http://", "")
        self.integration_log_service = IntegrationLog(processId=process_id,
                                                      URL=url,
                                                      userName=user_name,
                                                      password=password,
                                                      logLevelName=log_level_name)

    def _add_logs(self):
        self.integration_log_service.add(logLevel=LogLevel.INFO, message='Test1', description='TestD1')
        self.integration_log_service.add(logLevel=LogLevel.DEBUG, message='Test2', description='TestD2')
        self.integration_log_service.add(logLevel=LogLevel.WARNING, message='Test3', description='TestD3')
        self.integration_log_service.add(logLevel=LogLevel.ERROR, message='Test4', description='TestD4')

    def start(self):
        for i in range(3):
            time.sleep(5)
            self._add_logs()
            print(i, flush=True)
