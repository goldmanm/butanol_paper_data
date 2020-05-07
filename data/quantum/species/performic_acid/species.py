#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 1

energy = {
    'CBS-QB3': GaussianLog('p05_b.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('p05_b_f12.out'),
}

frequencies = GaussianLog('p05_bfreq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[3,4], top=[1,2,3]),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[1,3], top=[1,2]),	  
		]
