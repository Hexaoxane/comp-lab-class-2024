#!/bin/bash
#SBATCH --job-name=remd_simulation    # 任务名称
#SBATCH --output=remd_simulation.out  # 标准输出文件
#SBATCH --error=remd_simulation.err   # 标准错误输出文件
#SBATCH --partition=short             # 选择合适的分区
#SBATCH --ntasks=3                    # 运行的任务数量（3个温度）
#SBATCH --cpus-per-task=4             # 每个任务使用的CPU数量
#SBATCH --time=04:00:00               # 任务运行时间上限 (例如 4 小时)
#SBATCH --mem-per-cpu=8GB             # 每个CPU分配的内存

# 加载GROMACS模块
module load gromacs/openmpi/intel/2023.3

# 运行平行回火模拟
srun gmx_mpi mdrun -s adp -multidir T300/ T400/ T600/ -deffnm adp_exchange3temps -replex 500

