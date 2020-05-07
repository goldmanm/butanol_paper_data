#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 2

energy = {
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('TSN04_f12.out'),
}

frequencies = GaussianLog('ts8-freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[3,1], top=[1,2], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[5,12], top=[12,13,14,15,16], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[12,15], top=[15,16], symmetry=1, fit='best'),
HinderedRotor(scanLog=ScanLog('scan_3.log'), pivots=[5,8], top=[8,9,10,11], symmetry=1, fit='best'),]
