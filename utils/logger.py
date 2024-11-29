import logging
import os

class Logger:
    def __init__(self):
        self.logger = logging.getLogger('pageLogger')
        self.setup_logger()

    def setup_logger(self):
        if not self.logger.hasHandlers():
            self.logger.setLevel(logging.DEBUG)

            # Обработчик для вывода логов в консоль
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)

            # Обработчик для записи логов в файл
            log_file_path = os.path.join(os.path.dirname(__file__), 'test_logs.log')  # Путь к файлу логов
            fh = logging.FileHandler(log_file_path)
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

    def get_logger(self):
        return self.logger
