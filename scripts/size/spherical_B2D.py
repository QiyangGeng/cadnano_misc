"""
    File name: spherical_B2D.py
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
cL = 1/4*np.pi                          # conversion factor for long side
cS = 1/nE*np.pi                         # conversion factor for short side
D = B/(nH*nE*(cL*2+cS)/conv)            # diameter in nm
print('D = ' + str(D))
