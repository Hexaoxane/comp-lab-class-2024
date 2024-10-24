#!/bin/bash
#SBATCH --job-name=gromacs_md         # 作业名称
#SBATCH --nodes=1                     # 使用1个节点
#SBATCH --ntasks-per-node=8           # 每个节点分配8个任务（核心）
#SBATCH --cpus-per-task=1             # 每个任务使用1个CPU核心
#SBATCH --mem=32GB                    # 每个节点的内存
#SBATCH --time=4:00:00                # 运行时间限制（格式为小时:分钟:秒）
#SBATCH --output=gromacs_md.out       # 标准输出文件
#SBATCH --error=gromacs_md.err        # 错误输出文件

# 加载GROMACS和MPI模块
module load gromacs/openmpi/intel/2023.3

# 进入作业目录（替换为你的目录）
cd /scratch/hz3883/week5/comp-lab-class-2024/Week5-ParallelTempering/T300

# 运行GROMACS，禁用CPU绑定
srun --cpu-bind=none gmx_mpi mdrun -s adp.tpr -deffnm adp

