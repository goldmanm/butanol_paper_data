#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 1

energy = {
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('CC=C_f12.out'),
}
frequencies = GaussianLog('CC=C_freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[1,2], top=[1,5,4,6], symmetry=3)]
