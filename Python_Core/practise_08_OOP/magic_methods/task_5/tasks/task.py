import os
import tempfile
from shutil import rmtree

class TempDir:
    def __enter__(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_dir = os.getcwd()
        os.chdir(self.temp_dir.name)
        return self.temp_dir.name

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.original_dir)
        self.temp_dir.cleanup()