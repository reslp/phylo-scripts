#!/bin/bash
echo "Starting Concatenator"
[ -f ./input_files/IDs_used_for_tree.txt ] && echo "Found taxon ID file" || exit
wd=$(pwd)
#mkdir tmp

for d in $(ls ./input_files/*.fas)
do
	echo "Working on file:"
	echo $d
	echo "...Reduce"
	./phylo-scripts/reduce.py ./input_files/IDs_used_for_tree.txt $d > tmp/reduced_${d:21}
	echo "...Align"
	mafft --genafpair --maxiterate 10000 --quiet tmp/reduced_${d:21} > tmp/aligned_reduced_${d:21} 
	rm tmp/reduced_${d:21}
	echo "...Replace"
	./phylo-scripts/replace.py tmp/aligned_reduced_${d:21} > tmp/replaced_${d:21} 
	rm tmp/aligned_reduced_${d:21}
done

echo "Create concatenated alignment"
./phylo-scripts/concat.py ./input_files/IDs_used_for_tree.txt tmp/*.fas > concat.fas
cp concat.fas input_files/
echo "Done"
exit

