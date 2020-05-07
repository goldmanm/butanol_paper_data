#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 2

energy = {
    'CBS-QB3': GaussianLog('TS06.log'),
'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('TS06_f12.out'),
}

frequencies = GaussianLog('TS06freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[1,7], top=[7,8,9,10], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[1,3], top=[3,4,5,6], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[1,11], top=[11,12,13,14,15,16], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_3.log'), pivots=[14,15], top=[15,16], symmetry=1),
		  ]
# ignoring second scan log because it could not converge and its energy is higher than 10kcal/mol 
#HinderedRotor(scanLog=ScanLog('TS06_scan2.log'), pivots=[11,14], top=[14,15,16], symmetry=1),

