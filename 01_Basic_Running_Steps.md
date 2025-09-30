All calculations are on 1x1x1 unitcell. 

## $\color{Red}{\textbf{STEPS: BaZrS3 }}$
1. Discrete KPOINTS file is created using python script for the selected high symmetry points.
2. SCF calculation is done with discrete KPOINTS file [ TIME = ].
3. NSCF calculation is done with the same KPOINTS [ TIME = 3 m 14.670s ].
4. Do sumo-bandplot and create band.dat file. 
5. For vasp-band plot, copy band.dat, KPOINTS and sumo-logfile to another folder. From the logfile, x=ticks are taken. This will give you the full VASP-BAND. Not just the wannierselected bands. Now we can also plot fermi-corrected vasp-band from this data. Use the python script to add fermi correction.
6. Fermi energy is copied to incar and wanniertags are added. Now again vasp-wann run [ TIME = 8m 50.163s ].

## $\color{Blue}{\textbf{BandStructure matching}}$
