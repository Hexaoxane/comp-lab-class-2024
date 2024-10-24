from pymol import cmd

# 加载所有PDB结构
cmd.load("/mnt/d/QM_E/week7/Inputs/Arp_Est/test_394f9/test_394f9_unrelaxed_rank_001_alphafold2_ptm_model_4_seed_007.pdb", "model_1")
cmd.load("/mnt/d/QM_E/week7/Inputs/Arp_Est/test_394f9/test_394f9_unrelaxed_rank_002_alphafold2_ptm_model_5_seed_000.pdb", "model_2")
cmd.load("/mnt/d/QM_E/week7/Inputs/Arp_Est/test_394f9/test_394f9_unrelaxed_rank_003_alphafold2_ptm_model_5_seed_007.pdb", "model_3")
cmd.load("/mnt/d/QM_E/week7/Inputs/Arp_Est/test_394f9/test_394f9_unrelaxed_rank_004_alphafold2_ptm_model_1_seed_007.pdb", "model_4")
cmd.load("/mnt/d/QM_E/week7/Inputs/Arp_Est/test_394f9/test_394f9_unrelaxed_rank_005_alphafold2_ptm_model_5_seed_005.pdb", "model_5")

# 对齐模型
cmd.align("model_2", "model_1")
cmd.align("model_3", "model_1")
cmd.align("model_4", "model_1")
cmd.align("model_5", "model_1")

# 显示为 cartoon 表示
cmd.show("cartoon", "model_1")
cmd.show("cartoon", "model_2")
cmd.show("cartoon", "model_3")
cmd.show("cartoon", "model_4")
cmd.show("cartoon", "model_5")

# 给每个模型上色
cmd.color("red", "model_1")
cmd.color("green", "model_2")
cmd.color("blue", "model_3")
cmd.color("yellow", "model_4")
cmd.color("magenta", "model_5")

# 设置白色背景
cmd.bg_color("white")

# 缩放视图
cmd.zoom()

# 保存图片
cmd.png("/mnt/d/QM_E/week7/Images/arp_est_vmd_visualization_windowed.png", dpi=300)
