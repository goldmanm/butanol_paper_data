#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 2

energy = {
    'CBS-QB3': GaussianLog('p07_adduct.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('p07_adduct_f12.out'),
}

frequencies = GaussianLog('p07_adductfreq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[2,8], top=[8,9,10,11], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[2,4], top=[4,5,6,7], symmetry=3),
		]
