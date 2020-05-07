#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 2
energy = {
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('p01_f12.out'),
}
frequencies = GaussianLog('prod2-freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[5,7], top=[7,8,13], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[5,9], top=[9,10,11,12], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[5,1], top=[1,2,3,4], symmetry=3, fit='best'),
]
