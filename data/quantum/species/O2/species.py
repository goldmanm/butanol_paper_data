#!/usr/bin/env python
# -*- coding: utf-8 -*-
linear = True

spinMultiplicity = 3

energy = {
	'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('energy.out'),
}

geometry = GaussianLog('O2freq.log')

frequencies = GaussianLog('O2freq.log')

rotors = []
