This repository contains data and code to accompany "Pressure-dependent kinetics of isobutanol peroxy isomers" by Mark Jacob Goldman, Nathan Wa-Wai Lee, Jesse H Kroll, William H Green.

The goal of this repository is to help others reproduce and build off of our work. Docker is the recommended way to replicate the calculations, though you can also replicate without docker on linux devices.

# Structure of database

The structure of the folders in this repository are as followed:

* **code**-code to run the code to generate figures
* **data**-contains data used to make the figures
  * **quantum**-files from quantum calculations used in this work
  * **lit_mechanisms**-mechanisms from other work compared with this work
  * **mech_generation**-the mechanisms generated in this work and the folder where generated mechanisms are created

# Code

Various files exist within the code repository. They are described below:

* **create_mechanism.sh**-a bash script for generating the thermo and kinetics from quantum files uing RMG
* **make_network_input_files.py**-a helper method for `compare_mechanism.sh` which generated Arkane input files
* **simulate_pdep_fate.ipynb**-a jupyter notebook with code for generating the major pressure dependent products at various temperatures and pressures (can use without generating new kinetics)
* **visualize_pdep_vars.ipynb**-a jupyter notebook with code for generating data from microcanonical rates (must run Arkane calculations to use)
* **compare high_p with Sarathy.ipynb**-a jupyter notebook that compares rates in this work with those in Sarathy et al. (can use without generating new kinetics)
* **generate_tables.ipynb**-a jupyter notebook that generates LaTeX code for the two tables in the publication
* **get_zador_arrhenius.ipynb**-a jupyter notebook with code for generated modified Arrhenius from published data
* **get_collision_limit_ho2_adduct.ipynb**-a jupyter notebook with code to estimate the collision limited rate for HO2 and isobutanal

# Building using Docker

A file `Dockerfile` contains instructions to generate an image with all the dependencies for simulating the results of the model. The instructions here were tested on Ubuntu 18.04 and Ubuntu 20.04, but will likely work on other linux distributions and operating systems. The instructions below reference unix terminal commands to generate the image and complete the calculations. You will first have to install the docker package. Once that is installed, build the docker image with 

```
docker build . -t butanol
```

You can then create a container from the image and then launch a terminal session with it.

```
docker container run -it -p 8888:8888 butanol
```

If desired, rerun the generation of high-pressure-limit and pressure-dependent kinetics with:

```
cd /home/paper_repo/code
./create_mechanism.sh
```

To access jupyter notebooks inside the container, create and run the server with

```
jupyter notebook --ip 0.0.0.0 --port 8888 --no-browser --allow-root
```

You can view the notebook in your web browser on the same device as the container with the URL `localhost:8888`.

# Required dependendencies

A file called environment.yml contains the list of python packages that were used in the generation of the methods, and the `conda` command can be used to generate an environment from this. In addition to this, you will need versions of [RMG-Py](https://github.com/goldmanm/RMG-Py/tree/64374493bdf8cab36d3ed7ca815c71c76a13fe73) and [RMG-database](https://github.com/ReactionMechanismGenerator/RMG-database/tree/d626e2bd535faf1cb4c3c1618cfff8ad1bbe3dd9). The version of RMG contains additional file changes not available in the main RMG releases, which allow for longer names of molecules and storage of intemediate pressure-dependent values. Using a released version of RMG will not have this extra functionality.

