# Set background color to white
color Display Background white

# Load the structure file (topology)
mol new "D:\\QM_E\\WEEK5\\Week5-ParallelTempering\\T300\\adp.gro" type gro

# Load the trajectory file
mol addfile "D:\\QM_E\\WEEK5\\Week5-ParallelTempering\\T300\\adp_exchange3temps.xtc" type xtc waitfor all

# Apply "Licorice" representation for a clean and detailed view of the molecule
mol modselect 0 top all
mol modstyle 0 top Licorice 0.3 12 12  # Adjust radius and bond resolution for clarity
mol modcolor 0 top Name                 # Color by atom name

# Use the built-in "Glass" material, as it's compatible and highlights structure well
mol modmaterial 0 top Glass

# Set up lighting and adjust the view for better visual effects
display projection orthographic
rotate x by 90
rotate y by 180
scale by 1.2

# Render the scene with ambient occlusion enabled for better shading
render TachyonInternal "D:\\QM_E\\WEEK5\\Week5-ParallelTempering\\T300\\alanine_dipeptide_image.tga"

# Optional: quit VMD after rendering
# quit
