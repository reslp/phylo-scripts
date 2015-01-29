#!/bin/sh
#This script is part of the phylo-script pipeline: github.com/reslp
#written by Philipp Resl 2015

###################################################################
# Provide the paths to your own files here:
IDFILE="IDs_used_for_tree.txt"
FASTAPATH="/Users/sinnafoch/Dropbox/original_sequence_files/" #path has to be absolute!!, all your single locus files need to be in that folder
FASTAFILES=( #list of single locus files
"A_ITS_all.fas"
"B_SSU_all.fas"
"C_LSU_all.fas"
"D_mtSSU_all.fas"
"E_MCM7_all.fas"
"F_RPB1_all.fas"
"G_RPB2_all.fas"
"H_ef1a_both_all.fas"
)
# no need to change anything below this point. But of course you can...
###################################################################

echo "Check if all files are present:"
for i in "${FASTAFILES[@]}";
do
 echo "Looking for file..." $FASTAPATH$i
 	if [ -f $FASTAPATH$i ];
 		then
 			echo "...Found"
 	else
 		echo "...Not Found. Abort."
 		exit
 	fi
done

echo "Looking for ID file"
[ -f ./$IDFILE ] && echo "...Found" || exit

echo "Reducing files to desired Taxa:"
for i in "${FASTAFILES[@]}";
do
./reduce.py $IDFILE $FASTAPATH$i > $i"_red"
done

echo "Aligning reduced files:"
for i in "${FASTAFILES[@]}";
do
mafft  --maxiterate 10000 $i"_red" > $i"_mafft"
done

echo "Clean up temporary files"
for i in "${FASTAFILES[@]}";
do
rm $i"_red" 
done

echo "Format files for concatenated alignment"
for i in "${FASTAFILES[@]}";
do
./replace.py $i"_mafft" > $i"_replaced"
done

echo "Clean up temporary files"
for i in "${FASTAFILES[@]}";
do
rm $i"_mafft" 
done

rm concat.fas

echo "Create concatenated alignment"
~/Dropbox/phylo_scripts/concat.py $IDFILE *_replaced > concat.fas
echo "Done"