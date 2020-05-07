#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 2

energy = {
    'CBS-QB3': GaussianLog('TS03.log'),
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('TS03_f12.out'),
}

frequencies = GaussianLog('TS03freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[4,8], top=[8,9,10,14], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[11,12], top=[12,13], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[6,15], top=[15,16], symmetry=1),
		  ]
