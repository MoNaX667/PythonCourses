from contextlib import ContextDecorator
import datetime

class LogFile(ContextDecorator):
    def __init__(self, log_file):
        self.log_file = log_file
        self.start_time = None

    def __enter__(self):
        self.start_time = datetime.datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = datetime.datetime.now()
        execution_time = end_time - self.start_time

        log_line = f"Start: {self.start_time} | Run: {execution_time} | An error occurred: {exc_val}\n"

        with open(self.log_file, 'a') as file:
            file.write(log_line)

        return False