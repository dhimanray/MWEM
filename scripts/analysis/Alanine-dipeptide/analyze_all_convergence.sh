#!/bin/bash

for i in 7
do
	cd cell_$i
	for j in 10 20 30 40 50 60 70 80 90
	do
		cp analysis.py analysis_$j.py
		sed -i "s/w.niters/$j/g" analysis_$j.py
		sed -i "s/weights.txt/weights_$j.txt/g" analysis_$j.py
		sed -i "s/trajectories.pkl/trajectories_$j.pkl/g" analysis_$j.py
		sed -i "s/trajectories_pruned.pkl/trajectories_pruned_$j.pkl/g" analysis_$j.py
		sed -i "s/crossings.pkl/crossings_$j.pkl/g" analysis_$j.py
		python analysis_$j.py
	done
	cd ..
done

