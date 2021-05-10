#!/bin/bash

# Set up simulation environment
source env.sh

# Clean up from previous/ failed runs
rm -rf traj_segs seg_logs istates west.h5 
mkdir   seg_logs traj_segs istates

#copy files to bstate directory for starting points
cp equilibration/distance.dat bstates/distance.dat
cp equilibration/equilibration.xml bstates/seg.xml


# Set pointer to bstate and tstate
BSTATE_ARGS="--bstate-file $WEST_SIM_ROOT/bstates/bstates.txt"
TSTATE_ARGS="--tstate-file $WEST_SIM_ROOT/tstate.file"

# Run w_init
$WEST_ROOT/bin/w_init \
  $BSTATE_ARGS \
  $TSTATE_ARGS \
  --segs-per-state 5 \
  --work-manager=threads "$@"
