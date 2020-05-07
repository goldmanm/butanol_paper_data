#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 1

energy = {
    'CBS-QB3': GaussianLog('p03.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('p03_f12.out'),
}

frequencies = GaussianLog('p03freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[9,11], top=[11,12,13,14], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[3,1], top=[1,2], symmetry=1),
]
