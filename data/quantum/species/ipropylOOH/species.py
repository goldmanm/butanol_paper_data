#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 2

energy = {
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('CCCOO_f12.out'),
}
frequencies = GaussianLog('CCCOO_freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[5,6], top=[6,12]),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[4,5], top=[5,6,12]),
          HinderedRotor(scanLog=ScanLog('scan_2.log'), pivots=[2,4], top=[2,3,1,8,7,9]),
          HinderedRotor(scanLog=ScanLog('scan_3.log'), pivots=[1,2], top=[1,7,8,9]),]
