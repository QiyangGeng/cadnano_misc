"""
    File name: spherical_D2B.py
    Author: Qiyang Geng
    Date created: 2022/02/12
    Date last modified: 2022/02/12
    Python Version: 3.9
"""

import numpy as np

# Parameters
D = 100                                 # diameter in nm
nE = 3                                  # number of edges
nH = 6                                  # number of helices per edge


conv = 0.664                            # conversion factor in nm/nt
nL = D/4*np.pi/conv                     # length of longer edges in nt
nS = D/nE*np.pi/conv                    # length of shorter edges in nt
nB = nH*nE*(nL*2+nS)                    # number of nucleotides for the scaffold
print('nB = ' + str(nB))
