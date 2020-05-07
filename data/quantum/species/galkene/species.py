#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 1
opticalIsomers = 1
energy = {
    'CBS-QB3': GaussianLog('p3.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('p3_f12.out'),
}
frequencies = GaussianLog('p3freq.log')
rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[4,10], top=[10,11,12,13], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[8,5], top=[8,9], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[5,4], top=[5,6,7,8,9], symmetry=1)]
