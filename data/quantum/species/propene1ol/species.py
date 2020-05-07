#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 1
energy = {
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('p15_f12.out'),
}
frequencies = GaussianLog('p15freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[7,9], top=[9,10], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[1,5], top=[1,2,3,4], symmetry=3, fit='best'),
]
