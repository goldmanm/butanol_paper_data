#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 2
energy = {
    'CBS-QB3': GaussianLog('p9.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('p9_f12.out'),
}
frequencies = GaussianLog('p9freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[1,5], top=[5,6,7,8], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[15,12], top=[15,16], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[1,12], top=[12,13,14,15,16], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_3.log'), pivots=[9,1], top=[9,10,11], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_4.log'), pivots=[10,9], top=[10,11], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_5.log'), pivots=[2,1], top=[2,3,4], symmetry=1)]
