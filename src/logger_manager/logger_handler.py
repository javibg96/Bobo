import logging
import os
import time
from ..exceptions import PathNotFoundError

# copiado de alvaro, tienes que entenderlo sino te va a tocar poner un basic config format


class LoggerManager:
    def __init__(self, name="main", file_path=None, level=20):
        self.logger = logging.getLogger(name)
        sh = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        sh.setFormatter(formatter)
        self._logger.addHandler(sh)
        self._logger.setLevel(level)

        if file_path is not None:
            if os.path.isdir(file_path):
                current_date_path = os.path.join(file_path, time.strftime("%Y-%m-%d"))
                if not os.path.isdir(current_date_path):
                    os.mkdir(current_date_path)
                fh = logging.FileHandler(
                    filename=os.path.join(current_date_path, "{0}_{1}.log".format(name, time.strftime("%H%M%S"))))
                fh.setFormatter(formatter)
                self._logger.addHandler(fh)
            else:
                raise PathNotFoundError("The path passed does not exist: {0}".format(file_path))

    def close_log(self):
        _ = [handler.close for handler in self.logger.handlers]
        self.logger.handlers = []

    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, value):
        self._logger = value
