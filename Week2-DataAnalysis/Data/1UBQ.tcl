# Load the protein structure file
mol new {D:/Comp_Lab/comp-lab-class-2024/Week2-DataAnalysis/Data/1UBQ_processed.pdb}

# Set the representation to cartoon
mol delrep 0 top
mol representation NewCartoon
mol color Structure  ;# Color based on secondary structure
mol material Glossy
mol addrep top

# Add a black outline around the protein structure and make the edges thicker
mol representation NewCartoon
mol color Structure
mol material Outline  ;# Use Outline material to add black edges
mol addrep top

# Adjust the line thickness for a thicker black edge
display rendermode GLSL  ;# Ensure you are in GLSL render mode for better control of the outline
mol representation NewCartoon
mol selection all
mol color Structure
mol material Outline
graphics top line 1.5  ;# Increase this value to make the outline thicker (1.5 for thicker black edges)

# Set the background color to white
display projection orthographic
color Display Background white

# Enable depth cueing for depth effect
display depthcue on
color Display DepthCue 0.5

# Set some basic lighting to improve visual appeal
light 0 on
light 1 on
light 2 on
light 3 on
light 4 on
light 5 on

# Adjust the material properties for a nicer effect
material change ambient Glossy 0.3
material change diffuse Glossy 0.7
material change specular Glossy 0.8
material change shininess Glossy 0.9
material change opacity Glossy 1.0

# Enable shadows for more realistic lighting
display shadows on

# Enable antialiasing to smooth out the edges
display antialias on

# Set up for ray tracing using the correct method (Tachyon or TachyonInternal)
render TachyonInternal image.tga

# Alternatively, you can output in a different format like PNG
render TachyonInternal image.png
