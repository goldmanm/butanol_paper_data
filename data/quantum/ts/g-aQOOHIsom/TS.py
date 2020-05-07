#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 2

energy = {
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('TSN07_f12.out'),
}

frequencies = GaussianLog('TSN07-freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[10,12], top=[12,13], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[4,6], top=[6,7,8,9], symmetry=3, fit='best'),]
