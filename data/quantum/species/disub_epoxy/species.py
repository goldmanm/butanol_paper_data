#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 1
energy = {
    'CBS-QB3': GaussianLog('p2.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('p2_f12.out'),
}
frequencies = GaussianLog('p2freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[4,8], top=[8,9,10,11], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[12,1], top=[12,13], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[1,4], top=[1,2,3,12,13], symmetry=1)]
