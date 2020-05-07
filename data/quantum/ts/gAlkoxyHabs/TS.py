#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 2

energy = {
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('f12.out'),
}
frequencies = GaussianLog('freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[8, 4], top=[8, 14, 15, 16]),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[7, 3], top=[7, 12, 13]),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[7, 12], top=[12, 13]),]
