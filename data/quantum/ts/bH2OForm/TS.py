#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 2
opticalIsomers = 1
energy = {
    'CBS-QB3': GaussianLog('TS11cbsqb3.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('energy.out'),
}

frequencies = GaussianLog('TS11freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[2,3], top=[3,4,5,6], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[2,9], top=[9,10,11,12], symmetry=3)]
