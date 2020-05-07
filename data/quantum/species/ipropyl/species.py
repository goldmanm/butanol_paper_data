#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 2

opticalIsomers = 1

externalSymmetry = 2

energy = {
    'CBS-QB3': GaussianLog('p05_a.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('p05_a_f12.out'),
}

frequencies = GaussianLog('p05_afreq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[5,7], top=[7,8,9,10], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[5,1], top=[1,2,3,4], symmetry=3),	  
		]
