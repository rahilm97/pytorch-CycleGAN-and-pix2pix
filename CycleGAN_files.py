import os
import fnmatch
import shutil
import numpy as np

rootdir = "/data/rahilm/pytorch-CycleGAN-and-pix2pix/results/CT_cyclegan/test_latest/images/"

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if fnmatch.fnmatch(file, '*real_B.png'):
            os.mkdir("/data/rahilm/pytorch-CycleGAN-and-pix2pix/results/CT_cyclegan/test_latest/real_B/")
            shutil.copy(file, "/data/rahilm/pytorch-CycleGAN-and-pix2pix/results/CT_cyclegan/test_latest/real_B/")


        if fnmatch.fnmatch(file, '*fake_B.png'):
            os.mkdir("/data/rahilm/pytorch-CycleGAN-and-pix2pix/results/CT_cyclegan/test_latest/fake_B/")
            shutil.copy(file, "/data/rahilm/pytorch-CycleGAN-and-pix2pix/results/CT_cyclegan/test_latest/fake_B/")
