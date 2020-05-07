#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 2

energy = {
    'BMK/cbsb7': GaussianLog('TS05bmk.log'),
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('TS05bmk_f12.out'),
}

frequencies = GaussianLog('TS05bmkfreq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[8,13], top=[13,14,15,16], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[8,4], top=[1,2,3,4,5,6,7], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[4,6], top=[6,7], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_3.log'), pivots=[4,3], top=[1,2,3], symmetry=1),
		  HinderedRotor(scanLog=ScanLog('scan_4.log'), pivots=[3,1], top=[1,2], symmetry=1),
		  ]
