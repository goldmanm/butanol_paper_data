#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 2

energy = {
    'CBS-QB3': GaussianLog('TS10cbsqb3.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('energy.out'),
}

frequencies = GaussianLog('freq.log')

rotors = [HinderedRotor(scanLog=GaussianLog('scan_0.log'), pivots=[6,7], top=[7,8,9,10], symmetry=3),
          HinderedRotor(scanLog=GaussianLog('scan_1.log'), pivots=[4,1], top=[4,5], symmetry=1),
          HinderedRotor(scanLog=GaussianLog('scan_2.log'), pivots=[1,6], top=[1,2,3,4,5], symmetry=1)]
