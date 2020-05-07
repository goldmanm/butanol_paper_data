#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 1
opticalIsomers = 1

energy = {
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('C=CCO_f12.out'),
}

frequencies = GaussianLog('C=CCO_freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[1,2], top=[1,5], symmetry=1),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[2,3], top=[3,4,8,9,10], symmetry=1)]
