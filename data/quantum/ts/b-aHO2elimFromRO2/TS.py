#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 2

energy = {
    'CBS-QB3': GaussianLog('TS5cbsqb3.log'),
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('TS5cbsqb3_f12.out'),
}

frequencies = GaussianLog('TS5freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[4,5], top=[5,6,7,8], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[4,1], top=[1,2,3,14], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[15,9], top=[15,16], symmetry=1)]
