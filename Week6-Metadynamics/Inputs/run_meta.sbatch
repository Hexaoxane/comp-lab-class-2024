#!/bin/bash
#SBATCH --job-name=plumed_meta
#SBATCH --output=plumed_meta_output.log
#SBATCH --error=plumed_meta_error.log
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --mem=8GB

source /scratch/work/courses/CHEM-GA-2671-2024fa/software/gromacs-2019.6-plumedSept2020/bin/GMXRC.bash.modules

gmx_mpi mdrun -s topol.tpr -plumed plumed_meta.dat -deffnm meta_run
