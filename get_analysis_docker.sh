#!/bin/bash
echo "Starting Concatenator"
echo "Make sure to specify the FULL path to your input folder containing single locus files and the IDs_used_for_tree file"
echo "Example command (container is called phylo): docker run -v /home/resl/my_sequences/:/input_files/ phylo"
echo "If you use the concat pipeline in a publication please cite:"
echo "Philipp Resl (2015): phylo-scripts: Python scripts for phylogenetics. release v0.1. available at: http://github.com/reslp DOI: 10.5281/zenodo.15983"
echo "Philipp Resl, Kevin Schneider, Martin Westberg, Christian Printzen, Zdeněk Palice, Göran Thor, Alan Fryday, Helmut Mayrhofer and Toby Spribille (2015) Diagnostics for a troubled backbone: testing topological hypotheses of trapelioid lichenized fungi in a large-scale phylogeny of Ostropomycetidae (Lecanoromycetes). Fungal Diversity 73: 239-258"

[ -f ./input_files/IDs_used_for_tree.txt ] && echo "Found taxon ID file" || exit
wd=$(pwd)
#mkdir tmp

for d in $(ls ./input_files/*.fas)
do
	echo "Working on file:"
	echo $d
	echo "...Reduce"
	./phylo-scripts/reduce.py ./input_files/IDs_used_for_tree.txt $d > tmp/reduced_${d:14}
	echo "...Align"
	mafft --genafpair --maxiterate 10000 --quiet tmp/reduced_${d:14} > tmp/aligned_reduced_${d:14} 
	rm tmp/reduced_${d:14}
	echo "...Replace"
	./phylo-scripts/replace.py tmp/aligned_reduced_${d:14} > tmp/replaced_${d:14} 
	rm tmp/aligned_reduced_${d:14}
done

echo "Creating concatenated alignment"
./phylo-scripts/concat.py ./input_files/IDs_used_for_tree.txt tmp/*.fas > concat.fas
cp concat.fas input_files/
echo "Concatenator is done."
exit

