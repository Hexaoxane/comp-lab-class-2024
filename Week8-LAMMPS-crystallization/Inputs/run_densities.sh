#!/bin/bash

# Loop over densities from 0.5 to 1.1 in steps of 0.1
for density in $(seq 0.5 0.1 1.1); do
    echo "Running simulation for density $density"
    
    # Set the density variable for LAMMPS and run the simulation
    lmp -var density $density -in 2dWCA.in -log "output_density_${density}.log"
done

