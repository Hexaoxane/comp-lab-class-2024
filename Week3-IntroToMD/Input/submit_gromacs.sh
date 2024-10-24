#!/bin/bash
#SBATCH --job-name=gromacs_md_10ns      # 作业名称
#SBATCH --output=gromacs_md_10ns.log    # 标准输出日志文件
#SBATCH --error=gromacs_md_10ns.err     # 错误日志文件
#SBATCH --ntasks=1                      # 任务数为1
#SBATCH --cpus-per-task=45              # 每个任务分配45个CPU核心
#SBATCH --mem=180G                      # 请求180GB内存
#SBATCH --time=24:00:00                 # 最大运行时间为24小时

# 加载 GROMACS 模块
module load gromacs/openmpi/intel/2023.3

# 运行 GROMACS 分子动力学模拟
gmx_mpi mdrun -deffnm trp_cage_md_10ns

