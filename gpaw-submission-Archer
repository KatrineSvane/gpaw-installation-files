#!/bin/bash --login

#PBS -N gpawPW-FPtest 
#PBS -l select=8
#PBS -q short
#PBS -l walltime=0:20:00
#PBS -A e05-surfin-wal  

export OMP_NUM_THREADS=1
ulimit -s unlimited
module swap PrgEnv-cray/5.2.56 PrgEnv-gnu/5.2.56
module load python-compute/2.7.6
module load gpaw-setups/0.9.20000
module load gpaw/1.0.0

export NPROC=`qstat -f $PBS_JOBID | awk '/Resource_List.mpiprocs/ {print $3}'`
 
cd $PBS_O_WORKDIR

aprun -n $NPROC gpaw-python relax.py

