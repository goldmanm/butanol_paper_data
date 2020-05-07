#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 1
energy = {
    'CBS-QB3': GaussianLog('p01.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('p01_f12.out'),
}
frequencies = GaussianLog('p01freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[1,2], top=[2,3,4,5], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[1,6], top=[6,7,8,9], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[10,13], top=[13,14], symmetry=1),
		]
