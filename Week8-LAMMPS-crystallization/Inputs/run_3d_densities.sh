#!/bin/bash

# Loop over densities from 0.8 to 1.5 in steps of 0.1
for density in $(seq 0.8 0.1 1.5); do
    echo "Running 3D WCA simulation for density $density"
    
    # Run the simulation with specified density
    lmp -var density $density -in 3dWCA.in -log "3dWCA_density_${density}.log"
done
