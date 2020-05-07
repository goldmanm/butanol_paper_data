#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'CBS-QB3': GaussianLog('p7.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('p7_f12.out'),
}

frequencies = GaussianLog('p7freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[7,6], top=[7,8,9,10], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[11,6], top=[11,12,13,14], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[15,6], top=[15,16], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_3.log'), pivots=[1,6], top=[1,2,3,4,5], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_4.log'), pivots=[4,1], top=[4,5], symmetry=1)]
