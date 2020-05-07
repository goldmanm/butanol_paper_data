#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 2

energy = {
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('TSN03_f12.out'),
}

frequencies = GaussianLog('ts7-freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[14,15], top=[15,16], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[4,9], top=[9,10,11,12,13], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[9,12], top=[12,13], symmetry=1, fit='best'),]
