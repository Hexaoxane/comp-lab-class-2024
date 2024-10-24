from pymol import cmd

# 设置背景为白色
cmd.bg_color("white")

# 加载 AlphaFold3 预测的 ATP 和 ADP 结合形式
cmd.load("/mnt/d/QM_E/week7/Inputs/2BTF/AF3_fold_atp_2protin_mg/fold_atp_2protin_mg_model_0.cif", "actin_profilin_atp")
cmd.load("/mnt/d/QM_E/week7/Inputs/2BTF/AF3_fold_adp_2protin_mg/fold_adp_2protin_mg_model_0.cif", "actin_profilin_adp")

# 设置颜色：ATP 和 ADP
cmd.color("cyan", "actin_profilin_atp")
cmd.color("magenta", "actin_profilin_adp")

# 对齐 ATP 和 ADP 结合结构
cmd.align("actin_profilin_adp", "actin_profilin_atp")

# 设置蛋白质为 cartoon 表示
cmd.show("cartoon", "actin_profilin_atp")
cmd.show("cartoon", "actin_profilin_adp")

# 为蛋白质设置渐变颜色 (通过链条或 B-factor 显示)
cmd.spectrum("b", "blue_white_red", "actin_profilin_atp")
cmd.spectrum("b", "blue_white_red", "actin_profilin_adp")

# 添加表面表示以展示整体表面结构
cmd.show("surface", "actin_profilin_atp")
cmd.show("surface", "actin_profilin_adp")
cmd.set("transparency", 0.5, "actin_profilin_atp")
cmd.set("transparency", 0.5, "actin_profilin_adp")

# 选择与 ATP 和 ADP 结合处的氨基酸（距离 5 Å）
cmd.select("near_atp", "actin_profilin_atp within 5 of resn ATP")
cmd.select("near_adp", "actin_profilin_adp within 5 of resn ADP")

# 为氨基酸显示 sticks 表示
cmd.show("sticks", "near_atp")
cmd.show("sticks", "near_adp")
cmd.color("yellow", "near_atp")
cmd.color("red", "near_adp")

# 设置整体视图居中
cmd.zoom()

# 保存图像到 Images 文件夹
cmd.png("/mnt/d/QM_E/week7/Images/actin_profilin_atp_adp_overlay_advanced.png", width=3840, height=2160, dpi=300, ray=1)

