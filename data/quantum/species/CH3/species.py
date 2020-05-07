#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 2

energy = {
    'BMK/cbsb7': GaussianLog('CH3bmk.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('CH3bmk_f12.out'),
}

frequencies = GaussianLog('CH3bmkfreq.log')

rotors = []
