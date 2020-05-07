#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 2

energy = {
    'CBS-QB3': GaussianLog('TS12.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('TS12_f12.out'),
}

frequencies = GaussianLog('TS12freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[7,9], top=[9,10,11,12], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[3,5], top=[5,6], symmetry=1),
		  ]
