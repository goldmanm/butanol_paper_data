source activate rmg_env3

echo "****** Making Arkane input files"
python make_network_input_files.py

echo "****** Generating alpha network"
cd ../data/mech_generation/alpha/
mkdir -p cantherm_output
python /home/RMG-Py/Arkane.py cantherm_pdep_input.py -o cantherm_output
echo "****** Generating beta network"
cd ../beta/
mkdir -p cantherm_output
python /home/RMG-Py/Arkane.py cantherm_pdep_input.py -o cantherm_output
echo "****** Generating gamma network"
cd ../gamma/
mkdir -p cantherm_output
python /home/RMG-Py/Arkane.py cantherm_pdep_input.py -o cantherm_output
echo "****** Generating high-p rates"
cd ../all/
mkdir -p cantherm_output_high_p cantherm_output_thermo
python /home/RMG-Py/Arkane.py cantherm_high_p_input.py -o cantherm_output_high_p
python /home/RMG-Py/Arkane.py cantherm_thermo_input.py -o cantherm_output_thermo

echo "****** Merging pdep models and thermo"
mkdir -p ../pdep_merged
cd ../pdep_merged
python /home/RMG-Py/scripts/mergeModels.py --model1 ../alpha/cantherm_output/chem.inp ../all/cantherm_output_thermo/species_dictionary.txt --model2 ../beta/cantherm_output/chem.inp ../all/cantherm_output_thermo/species_dictionary.txt --model3 ../gamma/cantherm_output/chem.inp ../all/cantherm_output_thermo/species_dictionary.txt --model4 ../all/cantherm_output_thermo/chem.inp ../all/cantherm_output_thermo/species_dictionary.txt

echo "****** Adding thermo to high p model"
mkdir -p ../../high_p_merged
cd ../../high_p_merged
python /home/RMG-Py/scripts/mergeModels.py --model1 ../all/cantherm_output_thermo/chem.inp ../all/cantherm_output_thermo/species_dictionary.txt --model2 ../all/cantherm_output_high_p/chem.inp ../all/cantherm_output_thermo/species_dictionary.txt

echo "****** Creating cantera files"
ck2cti --input chem.inp --output chem.cti
cd ../pdep_merged
ck2cti --input chem.inp --output chem.cti
cd with_second_O2
ck2cti --input chem.inp --output chem.cti

