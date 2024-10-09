1. Parallel_Temperature_vs_Time.ipynb:
    Description: This notebook visualizes the temperature changes over time for different replicas in the parallel tempering simulation. It analyzes how the replicas exchange temperatures and verifies if the temperature transitions are occurring as expected.

2. Potential_Energy_Surface.ipynb:
    Description: This notebook calculates and visualizes the potential energy surface (PES) for the alanine dipeptide system at different temperatures. It creates 2D histograms of dihedral angles and plots the free energy landscape using phi and psi values.

3. dihedral_angle.ipynb:
    Description: This notebook computes the phi and psi dihedral angles of the alanine dipeptide from the molecular dynamics trajectory. It plots these angles over time to monitor the conformational changes of the system.

4. Parallel_dihedral_angles.ipynb:
    Description: This notebook analyzes the dihedral angles for parallel tempering simulations across different temperatures. It overlays the dihedral angle plots for 300K, 400K, and 600K to compare the conformational space sampled at these temperatures.

5. Potential_energy_surface_difference.ipynb:
    Description: This notebook calculates the difference between potential energy surfaces (PES) at different temperatures. It highlights regions of significant differences using color mapping to help visualize the conformational variations induced by temperature changes.

6. replica_temp.ipynb:
    Description: This notebook uses the output of the demux.pl script to analyze how each replica's temperature changes over time in the parallel tempering simulation. It verifies the efficiency of temperature exchanges and plots the replica temperature profiles.

7. PARALLEL_potential_surface.ipynb:
    Description: This notebook generates and compares the potential energy surfaces for different temperatures in a parallel tempering setup. It provides a combined view and individual PES plots for 300K, 400K, and 600K to illustrate the differences in energy landscapes.

8. Parallel_Energy_Histograms.ipynb:
    Description: This notebook calculates and visualizes the energy histograms for each temperature in the parallel tempering simulation. It overlays the histograms to assess if the energy distributions overlap properly, a critical check for ensuring good sampling and exchanges between replicas.

9. Potential.ipynb:
    Description: This notebook processes the potential energy data from the MD simulations. It extracts and plots the potential energy as a time series to analyze the stability and behavior of the system during the simulation.
