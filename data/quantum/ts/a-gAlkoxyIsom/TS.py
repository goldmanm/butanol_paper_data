#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 2

energy = {
    'CBS-QB3': GaussianLog('TS15.log'),
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('TS15_f12.out'),
}
frequencies = GaussianLog('TS15freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[8,10], top=[10,11,12,13], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[3,4], top=[1,2,3], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[3,1], top=[1,2], symmetry=1),
		  ]
