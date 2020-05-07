#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 2

energy = {
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('energy.out'),
}

frequencies = GaussianLog('freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[7,4], top=[7,8], symmetry=1, fit='cosine'),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[2,4], top=[4,7,8,6,15], symmetry=1, fit='best'),          
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[1,2], top=[1,3,16,9,10,11], symmetry=1, fit='cosine'),
          HinderedRotor(scanLog=ScanLog('scan_3.log'), pivots=[9,10], top=[10,11], symmetry=1, fit='best'),]
