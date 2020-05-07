#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 2

energy = {
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('TS13_f12.out'),
}

frequencies = GaussianLog('TS13freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[4,7], top=[7,8], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[9,10], top=[10,11], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[2,1], top=[1,3,16,9,10,11], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_3.log'), pivots=[2,12], top=[12,13,14,15], symmetry=3, fit='best'),]
