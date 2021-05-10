import numpy as np
import os
import subprocess

milestones = [1.0,1.5,2.0,3.0,4.0,5.0,6.0,8.0,10.0,12.0,13.0]

for i in range(len(milestones)-1):

    left = milestones[i]
    right = milestones[i+1]

    middle = 0.5*(left + right)

    dir_name = 'cell_%d'%i

    os.system('cp -r template %s'%dir_name)

    os.system('cp milestones/reference_%d.pdb %s/equilibration/reference.pdb'%(i,dir_name))
    os.system('cp milestones/milestone_%d.pdb %s/equilibration/structure.pdb'%(i,dir_name))

    os.system('cp milestones/reference_%d.pdb %s/common_files/reference.pdb'%(i,dir_name))
    os.system('cp milestones/milestone_%d.pdb %s/common_files/structure.pdb'%(i,dir_name))


    subprocess.call(["sed -i 's/CENTER/%0.2f/g' %s/equilibration/colvars.in"%(middle,dir_name)], shell=True)

    subprocess.call(["sed -i 's/LOW/%0.2f/g' %s/common_files/colvars.in"%(left,dir_name)], shell=True)
    subprocess.call(["sed -i 's/HIGH/%0.2f/g' %s/common_files/colvars.in"%(right,dir_name)], shell=True)

