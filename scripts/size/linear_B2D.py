"""
    File name: linear_B2D.py
    Author: Qiyang Geng
    Date created: 2022/02/12
    Date last modified: 2022/02/12
    Python Version: 3.9
"""

import numpy as np

# Parameters
B = np.array([7249, 7560, 8064])        # number of nucleotides for the scaffold
nE = 3                                  # number of edges
nH = 6                                  # number of helices per edge


conv = 0.664                            # conversion factor in nm/nt
cL = 1/2*np.sqrt(2)                     # conversion factor for long side
cS = np.sin(np.pi/nE)                   # conversion factor for short side
D = B/(nE*nH*(cS+2*cL)/conv)            # diameter in nm
print('D = ' + str(D))
