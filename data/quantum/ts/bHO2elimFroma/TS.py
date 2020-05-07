#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 2

energy = {
    'CBS-QB3': GaussianLog('TS6cbsqb3.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('TS6cbsqb3_f12.out'),
}

frequencies = GaussianLog('TS6freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[5,6], top=[6,7,8,9], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[10,5], top=[10,11,12,13], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[3,1], top=[3,4], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_3.log'), pivots=[14,5], top=[14,15,16], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_4.log'), pivots=[15,14], top=[15,16], symmetry=1)]
