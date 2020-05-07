#!/usr/bin/env python
# -*- coding: utf-8 -*-

spinMultiplicity = 2

energy = {
    'BMK/cbsb7': GaussianLog('Hbmk.log'),
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('Hbmk_f12.out'),
}

geometry = GaussianLog('Hbmkfreq.log')

frequencies = GaussianLog('Hbmkfreq.log')

rotors = []
