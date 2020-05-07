#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 1

opticalIsomers = 1
energy = {
    'BMK/cbsb7': GaussianLog('p02bmk.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('p02bmk_f12.out'),
}
frequencies = GaussianLog('p02bmkfreq.log')

rotors = [HinderedRotor(scanLog=GaussianLog('02methyl_scan.log'), pivots=[6,12], top=[12,13,14,15], symmetry=3),
          HinderedRotor(scanLog=GaussianLog('03methyl_scan.log'), pivots=[6,8], top=[8,9,10,11], symmetry=3),
          HinderedRotor(scanLog=GaussianLog('p02bmk_scan1.log'), pivots=[4,3], top=[1,2,3], symmetry=1),
          HinderedRotor(scanLog=GaussianLog('p02bmk_scan3.log'), pivots=[6,4], top=[1,2,3,4,5], symmetry=1),
          HinderedRotor(scanLog=GaussianLog('p02bmk_scan2.log'), pivots=[3,1], top=[1,2], symmetry=1),		  
		]
