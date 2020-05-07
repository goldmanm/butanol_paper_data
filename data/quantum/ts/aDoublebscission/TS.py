#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 2

energy = {
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('TS18_f12.out'),
}

frequencies = GaussianLog('TS18freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[7, 1], top=[1, 8]),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[2, 3], top=[2, 12]),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[6, 5], top=[5, 9, 13, 14], symmetry=3),]
