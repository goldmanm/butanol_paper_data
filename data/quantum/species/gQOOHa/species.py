#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 2

energy = {
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('p08_f12.out'),
}

frequencies = GaussianLog('g-Q1-freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[14,15], top=[15,16], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[1,14], top=[14,15,16], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[4,1], top=[1,2,3,14,15,16], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_3.log'), pivots=[4,10], top=[10,11,12,13], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_4.log'), pivots=[10,12], top=[12,13], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_5.log'), pivots=[4,6], top=[6,7,8,9], symmetry=3, fit='best'),
]
