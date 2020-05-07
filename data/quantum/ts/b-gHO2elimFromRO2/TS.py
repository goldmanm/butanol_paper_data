#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 2

energy = {
    'CBS-QB3': GaussianLog('TS4cbsqb3.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('TS4cbsqb3_f12.out'),
    #'CCSD(T)-F12/cc-pVTZ-F12':-382.93281171650256
}

frequencies = GaussianLog('TS4freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[7,6], top=[7,8,9,10], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[4,1], top=[4,5], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[1,6], top=[1,2,3,4,5], symmetry=1)]
