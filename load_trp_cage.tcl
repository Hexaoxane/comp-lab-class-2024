# Load the GRO file from the specified path
mol new "D:/comp-lab-class-2024/Week3-IntroToMD/trp_cage_nvt.gro" type gro

# Set representation for the protein
# Display the protein as a cartoon with a smooth color gradient
mol delrep 0 top
mol representation NewCartoon 0.3 10 0.3 0
mol color Structure
mol selection "protein"
mol material Opaque
mol addrep top

# Set representation for water molecules as small transparent spheres
mol representation VDW 0.2
mol color Name
mol selection "water"
mol material Transparent
mol addrep top

# Optional: If you want to emphasize ions or other components, you can add them with specific representations
# Example for ions:
# mol representation Licorice 0.1 10 10
# mol color Name
# mol selection "ions"
# mol material Opaque
# mol addrep top

# Center the protein and scale the view for better visualization
display projection orthographic
display resetview

# Adjust background color to white for better visibility (optional)
color Display Background white

