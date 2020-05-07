#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 1

opticalIsomers = 1
externalSymmetry = 1
energy = {
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('p03_f12.out'),
}

frequencies = GaussianLog('g-cyclo2-freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[10,13], top=[13,14], symmetry=1, fit='best'),
# Redo to frozen scan
HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[10,1], top=[10,11,12,13,14], symmetry=1, fit='best')]
