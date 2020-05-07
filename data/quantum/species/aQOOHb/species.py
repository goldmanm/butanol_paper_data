#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 2

energy = {
    'CBS-QB3': GaussianLog('p10.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('p10_f12.out'),
}

frequencies = GaussianLog('p10freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[8,13], top=[13,14,15,16], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[8,9], top=[9,10,11,12], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[4,8], top=[1,2,3,4,5,6,7], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_3.log'), pivots=[4,6], top=[6,7], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_4.log'), pivots=[3,4], top=[1,2,3], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_5.log'), pivots=[3,1], top=[1,2], symmetry=1)
		]
