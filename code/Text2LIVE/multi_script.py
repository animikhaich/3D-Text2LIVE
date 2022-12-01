from glob import glob
import os

files = sorted(glob("data/images/chair/train/*.png"))[62:]
for i, filepath in enumerate(files):
    print(f"Processing File: {i+1}/{len(files)} | Completed: {round(i+1/len(files)*100, 2)}%")
    os.system(f"python custom_train.py --example_config nerf_chair.yaml --file_path {filepath}")
