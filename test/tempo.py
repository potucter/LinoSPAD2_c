import numpy as np
import os
import pandas as pd

path = "C:/Users/bruce/Documents/Quantum astrometry/LinoSPAD/Software/"\
    "Data/40 ns window, 20 MHz clock, 10 cycles/10 lines of data/binary"

os.chdir(path)

filename = "goomba.csv"

data = np.arange(1, 6, 0.5)
data = pd.Series(data)
data_csv = pd.DataFrame(data)

# try:
#     aa = pd.read_csv(filename)
#     aa.insert(2, column=filename, value=data)
# except:
#     data_csv.to_csv(filename)
    
for i in range(5):
    data = np.arange(0,5*i, 1)
    data = pd.Series(data)
    data_csv = pd.DataFrame(data)
    try:
        aa = pd.read_csv(filename)
        aa.insert(loc=0, column = "{}:{}".format(i, filename), value=data,
                  allow_duplicates=True)
        aa.to_csv(filename, index=False)
    except:
        data_csv.to_csv(filename)

# =============================================================================
# 
# =============================================================================
os.chdir("C:/Users/bruce/Documents/Quantum astrometry/LinoSPAD/Software/Data/"\
         "40 ns window, 20 MHz clock, 10 cycles/10 lines of data/binary/"\
         "results")
filename = glob.glob('*timestamp_diff*')
Data = np.genfromtxt(filename[0])

data = []
for i in range (len(Data)):
    if np.abs(Data[i]) > 100:
        continue
    else:
        data.append(Data[i])
        
# =============================================================================
#
# =============================================================================
os.chdir('results')
# open csv file with results and add a column
print("\nSaving the data to the 'results' folder.")
output_csv = pd.Series(output)

filename = glob.glob('*timestamp_diff*')
if not filename:
    with open('timestamp_diff.csv', 'w'):
        filename = glob.glob('*timestamp_diff*')
        pass


os.chdir('..')
DATA_FILES = glob.glob('*dat*')
os.chdir('results')
r = 0
try:
    csv = pd.read_csv(filename[0])
    csv.insert(loc=0, column="{}".format(DATA_FILES[r]),
               value=output_csv, allow_duplicates=True)
    csv.to_csv(filename[0], index=False)
except Exception:
    output_csv.to_csv(filename[0], header=['{}'.format(DATA_FILES[r])],index=False)
os.chdir('..')       