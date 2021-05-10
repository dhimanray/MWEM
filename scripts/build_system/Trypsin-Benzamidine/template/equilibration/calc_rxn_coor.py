import numpy as np


l = np.loadtxt('milestone_equilibration.colvars.traj')

for i in range(len(l)):
    r = l[i,1]
    rmsd = l[i,2]
    print("{:.2f}".format(r), "{:.2f}".format(rmsd))
