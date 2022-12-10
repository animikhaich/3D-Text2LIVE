from glob import glob
import os
import time
import numpy as np
from datetime import timedelta


FILES = sorted(glob("/home/ani/Projects/3D-Text2LIVE/data/lego/train/*.png"))
CONFIG = "nerf_lego.yaml"



duration_history = list()
num_files = len(FILES)
for i, filepath in enumerate(FILES):
    start_time = time.time()
    os.system(f"echo 'Processing File: {i+1}/{len(FILES)} | Completed: {round((i+1)/len(FILES)*100, 2)}%'")
    os.system(f"python custom_train.py --example_config {CONFIG} --file_path {filepath}")

    # Get ETA
    end_time = time.time()
    duration_history.append(end_time - start_time)
    mean_duration = np.mean(duration_history)
    time_elapsed = np.sum(duration_history)
    time_eta = mean_duration * (num_files - i + 1)

    os.system(f"echo 'Time Spent: {str(timedelta(seconds=int(time_elapsed)))} | ETA: {str(timedelta(seconds=int(time_eta)))}'")