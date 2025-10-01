All calculations are on 1x1x1 BaZrS3 unitcell. 

## $\color{Magenta}{\textbf{ BaZrS3 - Basic Running Steps}}$
1. Discrete KPOINTS file is created using python script for the selected high symmetry points.
2. SCF calculation is done with discrete KPOINTS file [ TIME = ].
3. NSCF calculation is done with the same KPOINTS [ TIME = 3m 14.670s ].
4. Do sumo-bandplot and create band.dat file. 
5. For vasp-band plot, copy band.dat, KPOINTS and sumo-logfile to another folder. From the logfile, x=ticks are taken. This will give you the full VASP-BAND. Not just the wannierselected bands. Now we can also plot fermi-corrected vasp-band from this data. Use the python script to add fermi correction.
6. Fermi energy is copied to incar and wanniertags are added. Now again vasp-wann run [ TIME = 8m 50.163s ].
7. Then wannier90.x wannier90 is run [ TIME = 3m 51.916s ]. Again wannier90.x wannier90 is run with bandplot true command [ TIME = 0m 36.882s ].
8. Copy the wannier90_band.data and gnu files to a new folder. To compare with DFT band, take 56 bands from the fremicorrected_band.dat file. For that if the projected band starts from 2563th line, add (56*58) with that find 58th band. 56 is no of points in each band. Now plot DFT and Wannier together in one plot
9. Run postw90.x in different folder.For single temp [ TIME = 70h 11 m]

