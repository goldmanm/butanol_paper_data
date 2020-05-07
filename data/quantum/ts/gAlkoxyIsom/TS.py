#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 2

energy = {
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('TSN12_f12.out'),
}

frequencies = GaussianLog('ts12-freq.log')

rotors = [HinderedRotor(scanLog=GaussianLog('83methyl_scan.log'), pivots=[4,6], top=[6,7,8,9], symmetry=3, fit='best'),]
