#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 2

energy = {
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('TSN08_f12.out'),
}

frequencies = GaussianLog('ts2-freq.log')

rotors = [
HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[4,10], top=[10,11,12,13,14], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[10,13], top=[13,14], symmetry=1, fit='best'),
]
