#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 2

energy = {
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('energy.out'),
	#'CCSD(T)-F12/cc-pVTZ-F12':-382.9466871191517,
}

frequencies = GaussianLog('ts5-freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[1,2], top=[2,9,10,11], symmetry=3, fit='best'),
]
