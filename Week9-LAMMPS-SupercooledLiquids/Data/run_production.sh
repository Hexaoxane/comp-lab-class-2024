#!/bin/bash
#SBATCH --job-name=kalj_production
#SBATCH --output=kalj_production.out
#SBATCH --error=kalj_production.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=4
#SBATCH --time=0:30:00
#SBATCH --mem=24GB

source /scratch/work/courses/CHEM-GA-2671-2024fa/software/lammps-gcc-30Oct2022/setup_lammps.bash

temperatures=("1.5" "1.0" "0.9" "0.8" "0.7" "0.65" "0.6" "0.55" "0.5" "0.475")

for temp in "${temperatures[@]}"; do
    echo "Running production at temperature $temp"
    mpirun lmp -var configfile ../Inputs/n360/kalj_n360_T${temp}.lmp -var id 1 -in ../Inputs/production_3d_binary.lmp
done


