import os
import sys
import shutil
import subprocess
import time

# get the current working directory
current_dir = os.getcwd()

mvs_testing_dir = os.path.join(current_dir, "DTU_TESTING")

# get the list of folders in the Rectified directory
testing_folders = os.listdir(mvs_testing_dir)

for folder in testing_folders:
    # add commit and push to github
    subprocess.call(["git", "add", f"DTU_TESTING/{folder}"])
    subprocess.call(["git", "commit", "-m", "\"" + folder + "\""])
    subprocess.call(["git", "push"])

print(testing_folders)
