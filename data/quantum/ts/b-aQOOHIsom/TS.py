#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 2

energy = {
    'CBS-QB3': GaussianLog('TS7cbsqb3.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('TS7cbsqb3_f12.out'),
}

frequencies = GaussianLog('TS7freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[6,7], top=[7,8,9,10], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[6,11], top=[11,12,13,14], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[4,1], top=[4,5], symmetry=1)]
