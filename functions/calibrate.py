import numpy as np
import os
import glob
import pandas as pd


def calibrate_save(path, timestamps: int = 512):
    """
    Function for calculating the calibration matrix and saving it into a .csv
    file. The data file used for the calculation should be taken with the
    sensor uniformly illuminated by ambient light.

    Parameters
    ----------
    path : str
        Path to the data file.
    timestamps : int, optional
        Number of timestamps per acquisition cycle per pixel. The default is 512.

    Returns
    -------
    None.

    """

    os.chdir(path)
    filename = glob.glob("*.dat*")[0]

    # read data by 32 bit words
    rawFile = np.fromfile(filename, dtype=np.uint32)
    # lowest 28 bits are the timestamp; convert to ps
    data = (rawFile & 0xFFFFFFF).astype(int) % 140
    # mask nonvalid data with '-1'; 0x80000000 - the 31st, validity bin
    data[np.where(rawFile < 0x80000000)] = -1
    # number of acquisition cycles
    cycles = int(len(data) / timestamps / 256)

    data_matrix = (
        data.reshape(cycles, 256, timestamps)
        .transpose((1, 0, 2))
        .reshape(256, timestamps * cycles)
    )

    # calibration matrix
    cal_mat = np.zeros((256, 140))
    bins = np.arange(0, 141, 1)

    for i in range(256):
        # sort the data into 140 bins
        counts, bin_edges = np.histogram(data_matrix[i], bins=bins)
        # redefine the bin edges using the bin population from above
        cal_mat[i] = np.cumsum(counts) / np.cumsum(counts).max() * 2500
    cal_mat_df = pd.DataFrame(cal_mat)
    cal_mat_df.to_csv("Calibration_data.csv")


def calibrate_load(path):
    """
    Function for loading the calibration data.

    Parameters
    ----------
    path : str
        Path to the .csv file with the calibration matrix.

    Returns
    -------
    data_matrix : ndarray
        Matrix of 256x140 with the calibrated data.

    """

    os.chdir(path)

    file = glob.glob("*Calibration_data*")[0]

    data_matrix = np.genfromtxt(file, delimiter=",", skip_header=1)
    data_matrix = np.delete(data_matrix, 0, axis=1)
    return data_matrix