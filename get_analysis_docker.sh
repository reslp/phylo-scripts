#!/bin/bash
echo "Starting Concatenator"
echo
echo "Make sure to specify the FULL path to your input folder containing single locus files and the IDs_used_for_tree file"
echo
echo "Example command (container is called phylo): docker run -v /home/resl/my_sequences/:/input_files/ phylo"
echo

[ -f ./input_files/IDs_used_for_tree.txt ] && echo "Found taxon ID file" || exit
wd=$(pwd)
#mkdir tmp

echo
for d in $(ls ./input_files/*.fas)
do
	echo "Working on file: $d"
	echo "Calling reduce.py"
	./phylo-scripts/reduce.py ./input_files/IDs_used_for_tree.txt $d > tmp/reduced_${d:14}
	echo "Calling mafft"
	mafft --genafpair --maxiterate 10000 --quiet tmp/reduced_${d:14} > tmp/aligned_reduced_${d:14} 
	rm tmp/reduced_${d:14}
	echo "Calling replace.py"
	./phylo-scripts/replace.py tmp/aligned_reduced_${d:14} > tmp/replaced_${d:14} 
	rm tmp/aligned_reduced_${d:14}
done

echo
echo "Calling concat.py"
./phylo-scripts/concat.py ./input_files/IDs_used_for_tree.txt tmp/*.fas > concat.fas
cp concat.fas input_files/
echo
echo "Concatenator is done."
echo
echo "If you use the concat pipeline in a publication please cite:"
echo "1) Philipp Resl (2015): phylo-scripts: Python scripts for phylogenetics. release v0.1. available at: http://github.com/reslp DOI: 10.5281/zenodo.15983"
echo "2) Philipp Resl, Kevin Schneider, Martin Westberg, Christian Printzen, Zdeněk Palice, Göran Thor, Alan Fryday, Helmut Mayrhofer and Toby Spribille (2015) Diagnostics for a troubled backbone: testing topological hypotheses of trapelioid lichenized fungi in a large-scale phylogeny of Ostropomycetidae (Lecanoromycetes). Fungal Diversity 73: 239-258"
echo
exit

