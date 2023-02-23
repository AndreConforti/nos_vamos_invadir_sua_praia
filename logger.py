import logging
import dotenv
import os


class Logger:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.logger = logging.getLogger('Logger')
            cls._instance.logger.setLevel(logging.DEBUG)
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
            handler.setFormatter(formatter)
            cls._instance.logger.addHandler(handler)
            dotenv.load_dotenv()
        return cls._instance

    def log(self, level, message):
        #print(os.getenv("LOG_ENABLED"))
        if (os.getenv("LOG_ENABLED")==True):
            if level == "debug":
                self.logger.debug(message)
            elif level == "info":
                self.logger.info(message)
            elif level == "warning":
                self.logger.warning(message)
            elif level == "error":
                self.logger.error(message)
            elif level == "critical":
                self.logger.critical(message)
            else:
                raise Exception("Invalid log level")