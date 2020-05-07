#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 1

energy = {
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('OC=O_f12.out'),
}

frequencies = GaussianLog('OC=O_freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[1,2], top=[1,4], symmetry=1),]
