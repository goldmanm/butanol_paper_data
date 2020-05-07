#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 2
opticalIsomers = 1

energy = {
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('TS8c_f12.out'),
    #'CCSD(T)-F12/cc-pVTZ-F12': -382.9338341073141
}

frequencies = GaussianLog('TSfreq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[6,7], top=[7, 16]),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[2, 3], top=[3,11,12,13], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[1, 2], top=[1,8,9,10], symmetry=3),]
