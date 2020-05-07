#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 2

opticalIsomers = 1
externalSymmetry = 2

energy = {
    'CBS-QB3': GaussianLog('p5.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('p5_f12.out'),
}
frequencies = GaussianLog('p5freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[5,1], top=[1,2,3,4], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[5,6], top=[6,7,8,9], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[13,10], top=[13,14], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_3.log'), pivots=[5,10], top=[10,11,12,13,14], symmetry=1)]
