import os

class Cd:
    def __init__(self, directory):
        if not os.path.isdir(directory):
            raise ValueError(f"The directory '{directory}' does not exist or is not a directory.")
        self.directory = directory
        self.previous_directory = os.getcwd()

    def __enter__(self):
        os.chdir(self.directory)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.previous_directory)