Chemical Reaction Visualization Instructions
This document outlines the steps to generate images and a movie for the chemical reaction "before" and "after" states, using the provided simulation data.

File Paths
Input Files:

Topology: /mnt/d/QM_E/Week13-QMMM/Outputs/metad1_initmonitor/complex_LJ_mod.prmtop
Reaction Trajectory:
Before: /mnt/d/QM_E/Week13-QMMM/Outputs/metad1_initmonitor/METADYN-pos-00.xyz
After: /mnt/d/QM_E/Week13-QMMM/Outputs/metad1_initmonitor/METADYN-pos-03.xyz
Full Trajectory: /mnt/d/QM_E/Week13-QMMM/Outputs/metad1_initmonitor/METADYN-pos-*.xyz
Output Files:

Reaction before image: /mnt/d/QM_E/Week13-QMMM/Images/reaction_before.png
VMD script: /mnt/d/QM_E/Week13-QMMM/Scripts/reaction_visualization.vmd
Visualization Setup
Software: Use VMD.

Representation:

Protein: New Cartoon.
Ligand: Dynamic Bonds.
Protein side chains near the ligand: Licorice.
Visualization Steps:

Load the topology file and trajectory files.
Apply the specified representations.
Center the view on the ligand.
Image and Movie Generation
Images:

Use METADYN-pos-00.xyz for the "before" state.
Use METADYN-pos-03.xyz for the "after" state.
Save images via VMD's File > Render menu using TachyonInternal.
Movie:

Use VMD’s Extensions > Visualization > Movie Maker.
Select the full trajectory (METADYN-pos-*.xyz) and save the movie as an MPEG file.
Script Automation
To automate these steps, use the provided VMD script reaction_visualization.vmd:

tcl
mol new /mnt/d/QM_E/Week13-QMMM/Outputs/metad1_initmonitor/complex_LJ_mod.prmtop
mol addfile /mnt/d/QM_E/Week13-QMMM/Outputs/metad1_initmonitor/METADYN-pos-00.xyz type xyz waitfor all
mol addfile /mnt/d/QM_E/Week13-QMMM/Outputs/metad1_initmonitor/METADYN-pos-01.xyz type xyz waitfor all
mol addfile /mnt/d/QM_E/Week13-QMMM/Outputs/metad1_initmonitor/METADYN-pos-02.xyz type xyz waitfor all
mol addfile /mnt/d/QM_E/Week13-QMMM/Outputs/metad1_initmonitor/METADYN-pos-03.xyz type xyz waitfor all

mol modstyle 0 0 NewCartoon
mol modstyle 1 0 Licorice
mol modstyle 2 0 DynamicBonds
display resetview

render TachyonInternal /mnt/d/QM_E/Week13-QMMM/Images/reaction_before.png
render TachyonInternal /mnt/d/QM_E/Week13-QMMM/Images/reaction_after.png
Output Validation
Verify that the images show the ligand, protein, and surrounding side chains clearly.
Ensure the movie smoothly transitions through the trajectory.
Final Notes
These steps ensure reproducible visualization of the chemical reaction for publication or further analysis.