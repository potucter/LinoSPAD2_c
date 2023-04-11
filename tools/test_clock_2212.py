""" Testing the internal clock settings of the LinoSPAD2 firmware
version 2212/2208.
"""

import glob
import os

import numpy as np

from functions import unpack as f_up

path = "D:/LinoSPAD2/Data/board_A5/FW 2212 block/Spectrometer/Ar"

path = "C:/Users/bruce/Documents/Quantum astrometry/LinoSPAD/Software/release_2208/release_2208/mainstream/data"

os.chdir(path)

file = glob.glob("*.dat*")[0]

# data = f_up.unpack_2212(file, board_number="A5", fw_ver="block", timestamps=400)
data = f_up.unpack_numpy(file, board_number="NL11", timestamps=140)

# for i in range(len(data)):
#     check = 0
#     for j in range(len(data["{}".format(i)])):
#         if data["{}".format(i)][j] > check:
#             check = data["{}".format(i)][j]
#         elif data["{}".format(i)][j] < check and data["{}".format(i)][j] != -2:
#             print(i, j)
#             break
#         else:
#             continue

# 2208
timestamps = 140
for i in range(len(data)):
    check = 0
    for j in range(len(data[i])):
        if not j % timestamps:
            check = 0
        if data[i][j] > check:
            check = data[i][j]
        elif data[i][j] < check and data[i][j] != -1:
            print(i, j)
            break
        else:
            continue
