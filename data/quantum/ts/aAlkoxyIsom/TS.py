#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 2

energy = {
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('energy.out'),
}
frequencies = GaussianLog('freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[8, 10], top=[9, 10, 15, 5, 7, 12]),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[8, 3], top=[1,2,3,4], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[13,8], top=[11,13,14,16], symmetry=3),]
