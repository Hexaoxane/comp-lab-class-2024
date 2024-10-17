#!/bin/bash
#SBATCH --job-name=gmx_simulation      # 作业名称
#SBATCH --output=simulation_output.log # 输出文件名
#SBATCH --error=simulation_error.log   # 错误日志文件名
#SBATCH --ntasks=1                     # 任务数（一般设置为1）
#SBATCH --cpus-per-task=2              # 每个任务使用的CPU核数
#SBATCH --mem=4GB                     # 内存需求
#SBATCH --time=04:00:00                # 最大运行时间（例如4小时）

# 加载GROMACS模块
source /scratch/work/courses/CHEM-GA-2671-2024fa/software/gromacs-2019.6-plumedSept2020/bin/GMXRC.bash.modules

# 运行模拟
gmx_mpi mdrun -deffnm unbiased_run

