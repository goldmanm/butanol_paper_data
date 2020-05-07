#!/usr/bin/env python
# -*- coding: utf-8 -*-

opticalIsomers = 2

energy = {
    'CBS-QB3': GaussianLog('TS07.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('TS07_f12.out'),
    #'CCSD(T)-F12/cc-pVTZ-F12': -382.96546696009017
}
frequencies = GaussianLog('TS07freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[2,4], top=[4,5,6,7], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[2,8], top=[8,9,10,11], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[2,1], top=[1,12,13,14,15,16], symmetry=1),
		  ]
