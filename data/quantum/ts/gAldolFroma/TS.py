#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 2

energy = {
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('energy.out'),
}

frequencies = GaussianLog('freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[14,15], top=[15,16], symmetry=1, fit='best'),HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[4,6], top=[6,7,8,9], symmetry=3, fit='best'),]
