#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 2

energy = {
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('TSN05_f12.out'),
}
frequencies = GaussianLog('ts9-freq.log')

rotors = [HinderedRotor(scanLog=GaussianLog('scan_0.log'), pivots=[4,12], top=[12,13,14,15,16], symmetry=1, fit='best'),
HinderedRotor(scanLog=GaussianLog('scan_1.log'), pivots=[12,15], top=[15,16], symmetry=1, fit='best'),
HinderedRotor(scanLog=GaussianLog('scan_2.log'), pivots=[4,8], top=[8,9,10,11], symmetry=3, fit='best'),]
