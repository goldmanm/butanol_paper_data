#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'CBS-QB3': GaussianLog('p07.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('p07_f12.out'),
}

frequencies = GaussianLog('p07freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[1,3], top=[3,4,5,6], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[1,7], top=[7,8,9,10], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[1,11], top=[11,12,13], symmetry=1),
		]
