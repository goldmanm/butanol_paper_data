#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 2
energy = {
    'BMK/cbsb7': GaussianLog('p12bmk.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('p12bmk_f12.out'),
}
frequencies = GaussianLog('p12bmkfreq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[8,10], top=[10,11,12,13], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[8,14], top=[14,15,16], symmetry=2),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[8,4], top=[1,2,3,4,5,6,7], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_3.log'), pivots=[4,6], top=[6,7], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_4.log'), pivots=[3,4], top=[1,2,3], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_5.log'), pivots=[3,1], top=[1,2], symmetry=1)
		]
