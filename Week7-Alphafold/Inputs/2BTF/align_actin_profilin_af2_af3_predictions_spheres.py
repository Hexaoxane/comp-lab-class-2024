from pymol import cmd

# 设置白色背景
cmd.bg_color("white")

# 加载 ColabFold (AF2) 和 AlphaFold3 (AF3) 预测的结构
cmd.load("/mnt/d/QM_E/week7/Inputs/2BTF/AF2/test_2444f/test_2444f_unrelaxed_rank_001_alphafold2_multimer_v3_model_3_seed_000.pdb", "colabfold_af2")
cmd.load("/mnt/d/QM_E/week7/Inputs/2BTF/AF3_fold_atp_2protin_mg/fold_atp_2protin_mg_model_0.cif", "alphafold3_af3")

# 为 AF2 和 AF3 结构着色
cmd.color("blue", "colabfold_af2")
cmd.color("green", "alphafold3_af3")

# 对齐 AF2 到 AF3 结构
cmd.align("colabfold_af2", "alphafold3_af3")

# 显示表示法
cmd.show("cartoon", "colabfold_af2")
cmd.show("cartoon", "alphafold3_af3")

# 放大并居中显示
cmd.zoom()

# 保存对齐后的图像到 Images 文件夹
cmd.png("/mnt/d/QM_E/week7/Images/actin_profilin_af2_af3_alignment_spheres.png", width=3840, height=2160, dpi=300, ray=1)

