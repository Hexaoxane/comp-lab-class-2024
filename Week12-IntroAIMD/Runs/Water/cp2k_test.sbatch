#!/bin/bash
#SBATCH --job-name=cp2k
#SBATCH --nodes=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=18GB
#SBATCH --time=2:00:00

module load cp2k/openmpi/intel/20201212

mpirun -np 40 cp2k.popt -i water.inp -o OUTPUT_FILE_NAME.log
