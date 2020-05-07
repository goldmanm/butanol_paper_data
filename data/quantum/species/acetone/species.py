#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 1
energy = {
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('acetone_f12.out'),
}
frequencies = GaussianLog('acetonefreq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[1,5], top=[1,2,3,4], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[5,6], top=[6,7,8,9], symmetry=3)]
