#!/bin/bash
#SBATCH --job-name=cp2k
#SBATCH --ntasks=16
#SBATCH --cpus-per-task=2
#SBATCH --mem=80GB
#SBATCH --time=20:00:00

module load cp2k/openmpi/intel/20201212

mpirun -np 16 cp2k.popt -i water.inp -o water.log
