import os
import shutil
os.rename("test_file/content.txt","file.txt")
os.remove("test_file/logs.json")
shutil.rmtree("test_file/versioning")