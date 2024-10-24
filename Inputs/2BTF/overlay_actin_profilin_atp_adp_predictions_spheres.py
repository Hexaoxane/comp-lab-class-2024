from pymol import cmd

# 设置白色背景
cmd.bg_color("white")

# 加载 AlphaFold3 预测的 ATP 和 ADP 结合形式
cmd.load("/mnt/d/QM_E/week7/Inputs/2BTF/AF3_fold_atp_2protin_mg/fold_atp_2protin_mg_model_0.cif", "actin_profilin_atp")
cmd.load("/mnt/d/QM_E/week7/Inputs/2BTF/AF3_fold_adp_2protin_mg/fold_adp_2protin_mg_model_0.cif", "actin_profilin_adp")

# 为 ATP 和 ADP 绑定结构着色
cmd.color("cyan", "actin_profilin_atp")
cmd.color("magenta", "actin_profilin_adp")

# 对齐 ATP 和 ADP 绑定结构
cmd.align("actin_profilin_adp", "actin_profilin_atp")

# 显示表示法
cmd.show("spheres", "actin_profilin_atp")
cmd.show("spheres", "actin_profilin_adp")

# 放大并居中显示
cmd.zoom()

# 保存图像到当前文件夹下的 Images 文件夹
cmd.png("/mnt/d/QM_E/week7/Images/actin_profilin_atp_adp_overlay_spheres.png", width=3840, height=2160, dpi=300, ray=1)

