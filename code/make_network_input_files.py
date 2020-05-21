
import pandas as pd
import numpy as np
import os
from copy import deepcopy

import arkane
from rmgpy.molecule import Molecule

species_conversion_df = pd.read_csv('../data/species_name_comparison.csv',encoding='utf_8')
reactions_conversion_df = pd.read_csv('../data/reaction_info.csv',encoding='utf_8')
species2smiles = pd.Series(index=species_conversion_df['folder_name'],data=species_conversion_df['smiles'].values)
species2paper_name = pd.Series(index=species_conversion_df['folder_name'],data=species_conversion_df['chemkin_name'].values)

for network_name in ['alpha','beta','gamma','all']:
    base_folder = os.path.join('../data/mech_generation/',network_name)
    if not os.path.isdir(base_folder):
        os.makedirs(base_folder)
    pdep_string = ''
    high_p_string = ''
    thermo_string = ''
    assert os.path.isdir(base_folder), os.path.abspath(os.curdir)
    if network_name is not 'all':
        reactions = reactions_conversion_df[reactions_conversion_df.network == network_name]
    else:
        reactions = reactions_conversion_df
    reactions.fillna(False, inplace=True)
    network_species = set(reactions.R1) | set(reactions.R2) | set(reactions.Prod1) | set(reactions.Prod2) | set(reactions.Prod3)
    network_species.remove(False)

    # get input file string
    temp_string = '''
# coding=utf8

modelChemistry = 'CCSD(T)-F12/cc-pVTZ-F12//B3LYP/CBSB7'
useHinderedRotors = True
'''
    pdep_string += temp_string
    high_p_string += temp_string
    thermo_string += temp_string
    temp_string = 'useBondCorrections = False\n'
    pdep_string += temp_string
    high_p_string += temp_string
    thermo_string += 'useBondCorrections = True\n'

    # add species
    for s in network_species:
        # hack to get the hydrogen bonded adduct properly
        if isinstance(species2smiles[s],str) or isinstance(species2smiles[s], str):
            temp_string = u"""
species('{1}','../../quantum/species/{1}/species.py',
    structure = SMILES('{2}'),
    energyTransferModel = SingleExponentialDown(alpha0=(250,'cm^-1'), T0=(300,'K'), n=0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)
""".format(s,species2paper_name[s], species2smiles[s])
        else:
            temp_string = u"""
species('{1}','../../quantum/species/{1}/species.py',
    structure = SMILES('OC(O)C(O)C[CH2]'),
    molecularWeight = (105.11, 'g/mol'),
    energyTransferModel = SingleExponentialDown(alpha0=(250,'cm^-1'), T0=(300,'K'), n=0.85),    #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)
""".format(s,species2paper_name[s])

        pdep_string += temp_string
        high_p_string += temp_string
        thermo_string += temp_string + "thermo('{0}','nasa')\n".format(species2paper_name[s])

    # add bathgas (N2)
    pdep_string += """
species(
    label = "bath_gas",
    #structure = SMILES("N#N"),
    E0 = (0,'kJ/mol'),
    molecularWeight = (28.0062,"g/mol"),
    collisionModel = TransportData(sigma=(4.63691,"angstrom"), epsilon=(318.27557,'cm^-1')),
    energyTransferModel = None,
)
"""

    # add reactions
    networks = {}
    for reaction_num in reactions.index:
        # get info of reactants
        reaction_info = reactions.loc[reaction_num,:]
        reactants = [reaction_info.R1]
        if reaction_info.R2:
            reactants.append(reaction_info.R2)
        products = [reaction_info.Prod1]
        if reaction_info.Prod2:
            products.append(reaction_info.Prod2)
        if reaction_info.Prod3:
            products.append(reaction_info.Prod3)
        ts_file = reaction_info.TS
        rxn_name = reaction_info.ascii_name
        # save reaction information
        if ts_file:
            temp_string = """
transitionState('{0}','../../quantum/ts/{0}/TS.py')
reaction(
    label = '{0}',
    reactants = {1},
    products = {2},
    transitionState = '{0}',
    tunneling = 'Eckart',
)
""".format(rxn_name, [species2paper_name[s] for s in reactants], [species2paper_name[s] for s in products])
        else: # barrierless reaction
            if len(reactants) > 1:
                units = 'cm^3/(molecule*s)'
            else:
                units = 's^-1'
            temp_string = """
transitionState(
    label = '{0}',
    spinMultiplicity = 2,
    opticalIsomers = 2,
)
reaction(
    label = '{0}',
    reactants = {1},
    products = {2},
    transitionState = '{0}',
    kinetics = Arrhenius(A=({3},'{6}'), n={4}, Ea=({5},'K'), T0=(1,"K")),
)
""".format(rxn_name, 
                   [species2paper_name[s] for s in reactants], [species2paper_name[s] for s in products],
                   reaction_info.A, reaction_info.n, reaction_info.ea, units)
        pdep_string += temp_string
        high_p_string += temp_string

        # process network information if unimolecular
        if len(reactants) == 1 or len(products) == 1: 
            # find the potential energy surface of the rxn
            if len(reactants) == 1:
                atoms = Molecule().from_smiles(str(species2smiles[reactants[0]])).get_formula()
            else:
                # hack to work with the adduct, which doesn't have a SMILES structure
                try:
                    atoms = Molecule().from_smiles(str(species2smiles[products[0]])).get_formula()
                except ValueError:
                    atoms = Molecule().from_smiles(str('OC(O)C(O)C[CH2]')).get_formula()
            if atoms not in networks.keys():
                networks[atoms] = {'isomers': []}
            network = networks[atoms]
            # add reactants and products to the network object
            for species in [reactants, products]:
                if len(species) == 1:
                    if species2paper_name[species[0]] not in network['isomers']:
                        # add new species to list of isomers
                        network['isomers'].append(species2paper_name[species[0]])
                elif len(species) == 2:
                    if 'reactants' not in network.keys() and (species2paper_name[species[0]]=='O2' or species2paper_name[species[1]]=='O2'):
                        # only add one set of reactants, since cantherm will find all the products
                        network['reactants'] = [[species2paper_name[species[0]], species2paper_name[species[1]]]]

    # check than there is an entrance channel
    for name, network in networks.items():
        assert 'reactants' in network.keys(), 'no entrance channel found for network {}'.format(name)

    # add pdep network
    for name, network in networks.items():
        pdep_string += """
network(
    label = '{0}',
    isomers = {1},
    reactants = {2},
    bathGas = {{'bath_gas': 1.0}}
)
pressureDependence(
    '{0}',
    Tmin=(180.0,'K'), Tmax=(1500.0,'K'), Tcount=20,
    Pmin=(0.01,'bar'), Pmax=(100.0,'bar'), Pcount=20,
    maximumGrainSize = (0.5,'kcal/mol'),
    minimumGrainCount = 200,
    method = 'reservoir state',
    #method = 'modified strong collision',
    interpolationModel = ('chebyshev', 10, 8),
    activeKRotor = True, 
    activeJRotor = True,
    rmgmode = False,
)
""".format(name,network['isomers'],network['reactants'])

    # add high p rate constants
    for reaction_num in reactions.index:
        high_p_string += """
kinetics(
label = '{0}',
Tmin = (180,'K'), Tmax = (1500,'K'), Tcount = 20,
)
""".format(reactions.loc[reaction_num,'ascii_name'])

    # write the files
    with open(os.path.join(base_folder,'cantherm_high_p_input.py'),'w') as f:
        f.write(high_p_string)
    with open(os.path.join(base_folder,'cantherm_thermo_input.py'),'w') as f:
        f.write(thermo_string)
    with open(os.path.join(base_folder,'cantherm_pdep_input.py'),'w') as f:
        f.write(pdep_string)

