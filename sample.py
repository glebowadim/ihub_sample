import time

from onevizion import IntegrationLog, LogLevel

TEST_MESSAGE = "Test"
TEST_DESCRIPTION = "Test Description"


class Integration:

    def __init__(self, integration_log: IntegrationLog):
        self._integration_log_service = integration_log

    def start(self):
        for _ in range(3):
            time.sleep(5)
            self._integration_log_service.add(logLevel=LogLevel.INFO, message=TEST_MESSAGE,
                                              description=TEST_DESCRIPTION)
