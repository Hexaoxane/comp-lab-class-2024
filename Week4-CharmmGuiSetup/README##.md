Process for Completing the Lab 4 Assignment
# PS: I attempted a 10 ns simulation, but each time it failed. I tried adjusting the task time and the resources I called on GREENE, and even used input files from other students, but nothing seemed to work. So, I changed the task back to 1 ns, and it surprisingly succeeded, taking only ten minutes to complete. Since the deadline is approaching, I will have to process the data based on the 1 ns output. I apologize for this, and I will keep trying.

1. Set Up System Using CHARMMGUI:
    Access the CHARMMGUI Solution Builder and set up a system containing the miniprotein ArtEst (PDB ID: 1V1D).
    In Step 3 of CHARMMGUI, select AMBER as the force field and OPC water model. 
    Generate input files for GROMACS and set the temperature to 310 K.

2. Transfer and Untar Files on HPC:
    Download the final tarball (tgz) from CHARMMGUI and transfer it to the HPC under the directory `Week4/Setup`.
    Use the `tar` command to untar the files:
     bash
     tar xvf <filename>.tgz
     

3. Read GROMACS README and Script Comparison:
    Navigate to the GROMACS directory and read the provided README file.
    Copy the instructor's README.bash script and compare it to CHARMMGUI’s script to understand the differences.
   
4. Modify MDP File:
    Modify `step5_production.mdp` to run for 10 ns, ensuring that the total production run sums up to 50 ns.

5. Submit Job on HPC:
    Adjust the `sbatch` script to request 24 taskspernode, 1 cpupertask, and a 6hour runtime.
    Submit the job using the following command:
     bash
     sbatch run_setup.batch
     

6. Trajectory Processing:
    After completing the simulation, concatenate trajectories using `gmx trjcat` and wrap the protein with `gmx trjconv`. For example:
     bash
     gmx_mpi trjconv s step5_1.tpr f combined.xtc o wrapped.xtc pbc mol center
     

7. Data Analysis for Protein:
    Calculate endtoend distance of the protein using `gmx distance`:
     bash
     gmx_mpi distance s step5_1.tpr f protein_only.xtc oall end_to_end_dist.xvg
     

8. Set Up and Simulate NaCl System:
    Build a system with 0.1 M NaCl in a 50x50x50 Å³ box using CHARMMGUI, selecting CHARMM36M force field and NVT ensemble at 300 K.
    Modify `step5_production.mdp` to output snapshots every 10 ps.

9. Unwrap NaCl Trajectories:
    Use `gmx trjconv` to unwrap the NaCl trajectories with:
     bash
     gmx_mpi trjconv s step5_1.tpr f nacl_combined.xtc o unwrapped.xtc pbc nojump
     

10. MSD Calculation:
     Compute the Mean Squared Displacement (MSD) for water (OPC), Na+, and Cl using `gmx msd`. For example:
      bash
      gmx_mpi msd s step5_1.tpr f unwrapped.xtc n index.ndx o msd_water.xvg b 100 e 1000
      

11. Visualize Results:
     Use Python or Jupyter Notebook to plot endtoend distance and MSD results:
      python
      import matplotlib.pyplot as plt
      import numpy as np
      time, msd_na = np.loadtxt("msd_na.xvg", comments=["@", "#"], unpack=True)
      plt.plot(time, msd_na)
      plt.show()
      

12. Submit Assignment:
     Add sbatch scripts, MDP files, GRO files, Jupyter notebooks, and figures to your GitHub repository.
     Use the following commands to push changes to GitHub:
      bash
      git add .
      git commit m "Added Week 4 results"
      git push origin main
      

