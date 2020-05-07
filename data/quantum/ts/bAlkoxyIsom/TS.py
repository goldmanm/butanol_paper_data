#!/usr/bin/env python
# -*- coding: utf-8 -*-
spinMultiplicity = 2
opticalIsomers = 1

energy = {
    'CBS-QB3': GaussianLog('TS8cbsqb3.log'),
    'CCSD(T)-F12/cc-pVTZ-F12': MolproLog('energy.out'),
    #'CCSD(T)-F12/cc-pVTZ-F12': -382.94816667827337 # lowered by 2.5 kcal/mol till scaled calculation finishes. 
}

frequencies = GaussianLog('TS8freq.log')

rotors = [HinderedRotor(scanLog=ScanLog('scan_0.log'), pivots=[11,6], top=[11,12,13,14], symmetry=3),
          HinderedRotor(scanLog=ScanLog('scan_1.log'), pivots=[7,6], top=[7,8,9,10], symmetry=3)]
