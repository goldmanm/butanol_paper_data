#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 1
opticalIsomers = 1
energy = {
    'CBS-QB3': GaussianLog('p08.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('p08_f12.out'),
}
frequencies = GaussianLog('p08freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[5,11], top=[11,12,13,14], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[5,7], top=[7,8,9,10], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[3,1], top=[1,2], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_3.log'), pivots=[5,3], top=[1,2,3,4], symmetry=1),
		]
