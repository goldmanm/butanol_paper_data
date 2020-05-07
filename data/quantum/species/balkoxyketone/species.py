#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 2
energy = {
    'CBS-QB3': GaussianLog('p4.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('p11_f12.out'),
}
frequencies = GaussianLog('p11freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[2,9], top=[9,10,11,12], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[2,3], top=[3,4,5,6], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[2,7], top=[7,8, 13], symmetry=1)]
