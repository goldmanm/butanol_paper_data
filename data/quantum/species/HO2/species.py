#!/usr/bin/env python
# -*- coding: utf-8 -*-

linear = False

spinMultiplicity = 1

energy = {
    'CBS-QB3': GaussianLog('s00010103-opt.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('HO2_f12.out'),
}

geometry = GaussianLog('s00010103-freq.log')

frequencies = GaussianLog('s00010103-freq.log')

rotors = []
