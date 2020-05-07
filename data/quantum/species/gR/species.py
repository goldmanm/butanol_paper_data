#!/usr/bin/env python
# -*- coding: utf-8 -*-
linear = False

spinMultiplicity = 2

energy = {
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('p07_f12.out'),
}

frequencies = GaussianLog('iC4H9O-3-freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[10,13], top=[13,14], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[5,10], top=[10,11,12,13,14], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[5,7], top=[7,8,9], symmetry=2, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_3.log'), pivots=[5,1], top=[1,2,3,4], symmetry=3, fit='best'),
]
