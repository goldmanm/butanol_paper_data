#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 1
energy = {
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('p16_f12.out'),
}
frequencies = GaussianLog('p16freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[3,1], top=[1,2,12], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[3,9], top=[9,10,11,13,14], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[13,9], top=[13,14], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_3.log'), pivots=[5,3], top=[5,6,7,8], symmetry=3, fit='best'),
]
