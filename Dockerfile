#This is a sample Image 
FROM continuumio/miniconda3
RUN apt install git\
                gcc\
                g++\
                make


RUN git clone https://www.github.com/goldmanm/butanol_paper_data.git /home/paper_repo

RUN conda env create -f /home/paper_repo/environment.yml
RUN echo "source activate $(head -1 /home/paper_repo/environment.yml | cut -d' ' -f2)" > ~/.bashrc
ENV PATH /opt/conda/envs/$(head -1 /tmp/environment.yml | cut -d' ' -f2)/bin:$PATH

RUN git clone https://www.gitlab.com/goldmanm/RMG-Py.git /home/RMG-Py
RUN cd /home/RMG-Py
RUN git fetch origin butanol_py3_changes
RUN get reset 64374493bdf8cab --hard
RUN make
RUN git clone https://www.gitlab.com/ReactionMechanismGenerator/RMG-database.git /home/RMG-database
RUN cd /home/RMG-database
RUN get reset d626e2bd535faf1 --hard

ENV PATH /opt/conda/envs/$(head -1 /tmp/environment.yml | cut -d' ' -f2)/bin:/home/RMG-Py:$PATH
ENV PYTHONPATH "${PYTHONPATH}:/home/RMG-Py"

