#!/bin/bash
#SBATCH --job-name=sim_A             # 作业名称
#SBATCH --output=sim_A_output.log    # 输出文件名
#SBATCH --error=sim_A_error.log      # 错误日志文件名
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32GB
#SBATCH --time=06:00:00

# 加载GROMACS模块
source /scratch/work/courses/CHEM-GA-2671-2024fa/software/gromacs-2019.6-plumedSept2020/bin/GMXRC.bash.modules

# 运行模拟
gmx_mpi mdrun -s topolB.tpr -nsteps 10000000

