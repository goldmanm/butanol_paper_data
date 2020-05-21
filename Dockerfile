#This is a sample Image 
FROM continuumio/miniconda3
RUN apt update &&\
    apt install -y gcc\
                   g++\
                   make


RUN git clone https://www.github.com/goldmanm/butanol_paper_data.git /home/paper_repo

RUN conda env create -f /home/paper_repo/environment.yml
RUN echo "source activate $(head -1 /home/paper_repo/environment.yml | cut -d' ' -f2)" > ~/.bashrc

RUN git clone https://www.github.com/goldmanm/RMG-Py.git /home/RMG-Py &&\
    cd /home/RMG-Py &&\
    git fetch origin butanol_py3_changes &&\
    git reset 64374493bdf8cab --hard &&\
    /bin/bash -c "source activate rmg_env3; make"
RUN git clone https://www.github.com/ReactionMechanismGenerator/RMG-database.git /home/RMG-database &&\
    cd /home/RMG-database &&\
    git reset d626e2bd535faf1 --hard

ENV PATH="${PATH}:/home/RMG-Py"
ENV PYTHONPATH="${PYTHONPATH}:/home/RMG-Py"

