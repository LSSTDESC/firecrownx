#!/usr/bin/env python

import interpolation
import scipy as sc
import scipy.stats
from scipy.special import erf
import random as rd


try:
    import gi

    gi.require_version("NumCosmo", "1.0")
    gi.require_version("NumCosmoMath", "1.0")
except:
    pass

import math
from gi.repository import GObject
from gi.repository import NumCosmo as Nc
from gi.repository import NumCosmoMath as Ncm
import sys

sys.path.insert(0, "../../scripts")
import os
import numpy as np
from astropy.table import Table
from numpy import random
import scipy
import matplotlib.pyplot as plt
import clmm
from clmm import GalaxyCluster, ClusterEnsemble, GCData
from clmm import Cosmology
from clmm.support import mock_data as mock
import pandas as pd
import numpy as np
import pyccl as ccl
import sacc

clmm.__version__
import pandas as pd
from astropy.io import fits
from astropy.table import Table
import scipy.integrate
import astropy.units as u
import firecrown
from firecrown.models import richness_proxy

ncdata_fits = fits.open("ncount_nodist.fits")
ncdata_data = ncdata_fits[1].data

ncdata_Table = Table(ncdata_data)

lnM = np.array(ncdata_Table["LNM_TRUE"])
lnz = np.array(ncdata_Table["Z_TRUE"])
print(len(lnM))
lnN = np.linspace(0, 6, 500)
proxy = richness_proxy.RMProxy()
proxy.likelihood_parameters = [
    3.19,
    0.8685889638,
    -0.30400613733,
    0.33,
    -0.03474355855,
    0.0,
]
rich = []
lnN = np.array(lnN)
for a in range(0, 88706):
    filei = open('richness.txt','w')
    p_gauss = []
    lnMi = lnM[a]
    lnzi = lnz[a]
    for lnNi in lnN:
        pi_gauss = proxy.mass_proxy_likelihood(
            np.log10(np.exp(lnNi)),  # pylint: disable=invalid-name
            np.log10(np.exp(lnMi)),
            np.exp(lnzi),  # pylint: disable=invalid-name
            3.19,
            0.8685889638,
            -0.30400613733,
            0.33,
            -0.03474355855,
            0.0,
        )
        p_gauss.append(pi_gauss)
    generator = interpolation.LinearInterp(lnN, p_gauss, [0, 6])
    rich.append(generator.generate_random_point()[0])
    item = rich[a]
    print(item)
    filei.write(f"{item}\n")
    filei.close()
