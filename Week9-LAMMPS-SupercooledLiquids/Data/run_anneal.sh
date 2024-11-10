#!/bin/bash
#SBATCH --job-name=kalj_anneal
#SBATCH --output=kalj_anneal.out
#SBATCH --error=kalj_anneal.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=8
#SBATCH --mem=40GB
#SBATCH --time=3:00:00

source /scratch/work/courses/CHEM-GA-2671-2024fa/software/lammps-gcc-30Oct2022/setup_lammps.bash

mpirun lmp -var configfile ../Inputs/n360/kalj_n360_create.lmp -var id 1 -in ../Inputs/create_3d_binary.lmp

temperatures=("1.5" "1.0" "0.9" "0.8" "0.7" "0.65" "0.6" "0.55" "0.5" "0.475")

for temp in "${temperatures[@]}"; do
    mpirun lmp -var configfile ../Inputs/n360/kalj_n360_T${temp}.lmp -var id 1 -in ../Inputs/anneal_3d_binary.lmp
done
