#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 2

energy = {
    'CBS-QB3': GaussianLog('TS2cbsqb3.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('TS2cbsqb3_f12.out'),
}

frequencies = GaussianLog('TS2freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[5,1], top=[5,6,7,8], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[10,9], top=[10,11], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[15,12], top=[15,16], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_3.log'), pivots=[12,1], top=[12,13,14,15,16], symmetry=1)]
