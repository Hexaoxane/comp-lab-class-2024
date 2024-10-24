from pymol import cmd

# 设置背景为白色
cmd.bg_color("white")

# 加载 6ZSL 的晶体结构
cmd.load("/mnt/d/QM_E/week7/Inputs/NSP13/6zsl.pdb", "nsp13_crystal")

# 加载 AlphaFold 预测结构，分别来自 AF3_RNA_ATP_predict 文件夹
cmd.load("/mnt/d/QM_E/week7/Inputs/NSP13/AF3_RNA_ATP_predict/fold_2024_10_23_23_38_model_0.cif", "model_0")
cmd.load("/mnt/d/QM_E/week7/Inputs/NSP13/AF3_RNA_ATP_predict/fold_2024_10_23_23_38_model_1.cif", "model_1")
cmd.load("/mnt/d/QM_E/week7/Inputs/NSP13/AF3_RNA_ATP_predict/fold_2024_10_23_23_38_model_2.cif", "model_2")
cmd.load("/mnt/d/QM_E/week7/Inputs/NSP13/AF3_RNA_ATP_predict/fold_2024_10_23_23_38_model_3.cif", "model_3")
cmd.load("/mnt/d/QM_E/week7/Inputs/NSP13/AF3_RNA_ATP_predict/fold_2024_10_23_23_38_model_4.cif", "model_4")

# 为不同的模型设置颜色
cmd.color("blue", "model_0")
cmd.color("red", "model_1")
cmd.color("green", "model_2")
cmd.color("yellow", "model_3")
cmd.color("magenta", "model_4")

# 对齐预测结构到晶体结构
cmd.align("model_0", "nsp13_crystal")
cmd.align("model_1", "nsp13_crystal")
cmd.align("model_2", "nsp13_crystal")
cmd.align("model_3", "nsp13_crystal")
cmd.align("model_4", "nsp13_crystal")

# 显示表示法
cmd.show("cartoon", "nsp13_crystal")
cmd.show("cartoon", "model_0")
cmd.show("cartoon", "model_1")
cmd.show("cartoon", "model_2")
cmd.show("cartoon", "model_3")
cmd.show("cartoon", "model_4")

# 调整透明度以便更好地对比
cmd.set("cartoon_transparency", 0.3, "nsp13_crystal")
cmd.set("cartoon_transparency", 0.2, "model_0")
cmd.set("cartoon_transparency", 0.2, "model_1")
cmd.set("cartoon_transparency", 0.2, "model_2")
cmd.set("cartoon_transparency", 0.2, "model_3")
cmd.set("cartoon_transparency", 0.2, "model_4")

# 缩放并居中视图
cmd.zoom()

# 保存图像到指定路径，设置分辨率为4K（3840x2160）
cmd.png("/mnt/d/QM_E/week7/Images/nsp13_prediction_visualization_4k.png", width=3840, height=2160, dpi=300, ray=1)
``
