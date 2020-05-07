#!/usr/bin/env python
# -*- coding: utf-8 -*-

linear = True

spinMultiplicity = 2

energy = {
    'CBS-QB3': GaussianLog('s00010102-opt.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('OH_f12.out'),
}

geometry = GaussianLog('s00010102-freq.log')

frequencies = GaussianLog('s00010102-freq.log')

rotors = []
