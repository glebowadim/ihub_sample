from onevizion import IntegrationLog, LogLevel


class OVIntegration:

    def __init__(self, process_id: int, url: str, user_name: str, password: str, log_level_name: str):
        self.integration_log_service = IntegrationLog(processId=process_id,
                                                      URL=url,
                                                      userName=user_name,
                                                      password=password,
                                                      logLevelName=log_level_name)

    def add_log(self):
        self.integration_log_service.add(logLevel=LogLevel.INFO, message='Test1', description='TestD1')
        self.integration_log_service.add(logLevel=LogLevel.DEBUG, message='Test2', description='TestD2')
        self.integration_log_service.add(logLevel=LogLevel.WARNING, message='Test3', description='TestD3')
        self.integration_log_service.add(logLevel=LogLevel.ERROR, message='Test4', description='TestD4')
