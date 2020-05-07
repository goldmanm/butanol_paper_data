This repository contains data and code to accompany "Pressure-dependent kinetics of isobutanol peroxy isomers" by Mark Jacob Goldman, Nathan Wa-Wai Lee, Jesse H Kroll, William H Green.

The goal of this repository is to help others reproduce and build off of our work. This readme is organized into a few sections.

# Required dependendencies

A file called environment.txt contains the list of python packages that were used in the generation of the methods, and the `conda` command can be used to generate an environment from this. In addition to this, you will need versions of [RMG-Py]() and [RMG-database](). The version of RMG contains additional file changes not available in the main RMG releases, which allow for longer names of molecules and storage of intemediate pressure-dependent values. Using a released version of RMG will not have this extra functionality.

These calculations were done on Ubuntu 18.04, though other Unix-based OS's might also work.

# Structure of database

The structure of the folders in this repository are as followed:

* **code**-code to run the code to generate figures
* **data**-contains data used to make the figures
  * **quantum**-files from quantum calculations used in this work
  * **lit_mechanisms**-mechanisms from other work compared with this work
  * **mech_generation**-the mechanisms generated in this work and the folder where generated mechanisms are created

# Code

Various methods exist within the code repository. They are described below:

* **compare_mechanism.sh**-a bash script for generating the thermo and kinetics from quantum files uing RMG
* **make_network_input_files.py**-a helper method for `compare_mechanism.sh` which generated Arkane input files
* **simulate_pdep_fate.ipynb**-a jupyter notebook with code for generating the major pressure dependent products at various temperatures and pressures (can use without generating new kinetics)
* **visualize_pdep_vars.ipynb**-a jupyter notebook with code for generating data from microcanonical rates (must run Arkane calculations to use)
* **compare high_p with Sarathy.ipynb**-a jupyter notebook that compares rates in this work with those in Sarathy et al. (can use without generating new kinetics)
* **generate_tables.ipynb**-a jupyter notebook that generates LaTeX code for the two tables in the publication
* **get_zador_arrhenius.ipynb**-a jupyter notebook with code for generated modified Arrhenius from published data
* **get_collision_limit_ho2_adduct.ipynb**-a jupyter notebook with code to estimate the collision limited rate for HO2 and isobutanal

