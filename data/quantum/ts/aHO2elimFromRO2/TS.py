#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 2
energy = {
    'CBS-QB3': GaussianLog('TS08.log'),
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('TS08_f12.out'),
}
frequencies = GaussianLog('TS08freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[5,6], top=[6,7,8,9], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[5,10], top=[10,11,12,13], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[3,1], top=[1,2], symmetry=1),
		  ]
