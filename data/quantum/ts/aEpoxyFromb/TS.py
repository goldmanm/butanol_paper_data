#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 2
energy = {
    'CBS-QB3': GaussianLog('TS01.log'),
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('TS01_f12.out'),
}
frequencies = GaussianLog('TS01freq.log')

rotors = [HinderedRotor(scanLog=GaussianLog('scan_0.log'), pivots=[1,6], top=[6,7,8,9], symmetry=3),
          HinderedRotor(scanLog=GaussianLog('scan_1.log'), pivots=[1,2], top=[2,3,4,5], symmetry=3),
          HinderedRotor(scanLog=GaussianLog('scan_2.log'), pivots=[10,13], top=[13,14], symmetry=1),
          HinderedRotor(scanLog=GaussianLog('scan_3.log'), pivots=[12,15], top=[15,16], symmetry=1),
		  ]
