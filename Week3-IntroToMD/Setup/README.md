650  grep -v HOH 2JOF.pdb > 2JOF_clean.pdb   # Removed water molecules from 2JOF.pdb and saved to 2JOF_clean.pdb
652  gmx pdb2gmx -f 2JOF_clean.pdb -o 2JOF_processed.gro -water spce   # Generated GROMACS structure file using SPC/E water model
654  module load gromacs/openmpi/intel/2020.4   # Loaded the GROMACS 2020.4 version module
655  gmx pdb2gmx -f 2JOF_clean.pdb -o 2JOF_processed.gro -water spce   # Re-ran pdb2gmx to ensure correct water model
657  gmx pdb2gmx -f 2JOF_clean.pdb -o 2JOF_processed.gro -water spce   # Third time running pdb2gmx to confirm the file generation
659  gmx pdb2gmx -f 2JOF_clean.pdb -o 2JOF_processed.gro -water spce   # Processed the protein structure again
652  gmx editconf -f trp_cage_processed.gro -o trp_cage_box.gro -c -d 1.0 -bt cubic   # Defined cubic box size using editconf and centered the protein
661  which gormacs   # Attempted to locate the gromacs command
961  gmx_mpi solvate -cp trp_cage_box.gro -cs spc216.gro -o trp_cage_solvated.gro -p topol.top   # Solvated the protein in the box by adding water molecules
963  vim ions.mdp   # Opened ions.mdp to define parameters for ion addition
967  vim minim.mdp   # Edited minim.mdp to define parameters for energy minimization
973  gmx_mpi grompp -f npt.mdp -c trp_cage_nvt.gro -r trp_cage_nvt.gro -p topol.top -o trp_cage_npt.tpr   # Prepared input files for NPT equilibration
976  gmx_mpi grompp -f npt.mdp -c trp_cage_nvt.gro -r trp_cage_nvt.gro -p topol.top -o trp_cage_npt.tpr -maxwarn 1   # Ignored 1 warning to proceed with file preparation
1011  gmx energy -f trp_cage_nvt.edr -o temperature.xvg   # Extracted temperature vs time data
1012  gmx_mpi energy -f trp_cage_nvt.edr -o temperature.xvg   # Used MPI GROMACS to extract temperature data
1014  gmx_mpi grompp -f npt.mdp -c trp_cage_nvt.gro -r trp_cage_nvt.gro -t trp_cage_nvt.cpt -p topol.top -o trp_cage_npt.tpr   # Prepared NPT equilibration input files, using the checkpoint file
1015  gmx_mpi energy -f trp_cage_npt.edr -o pressure.xvg   # Extracted pressure data
1016  gmx_mpi energy -f trp_cage_npt.edr -o density.xvg   # Extracted density data
 
    # PS: due to some interuption, I can not find my whole history of process of manipulation on gromacs, I'll pay attention next week