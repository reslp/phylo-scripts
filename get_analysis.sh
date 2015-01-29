#!/bin/sh



echo "Starting Analysis"

echo "Check if all files are present:"
echo "Looking for file: ~/Dropbox/original_sequence_files/ITS_all.fas"
[ -f ~/Dropbox/original_sequence_files/A_ITS_all.fas ] && echo "Found ~/Dropbox/original_sequence_files/ITS_all.fas" || exit
echo "Looking for file: ~/Dropbox/original_sequence_files/SSU_all.fas"
[ -f ~/Dropbox/original_sequence_files/B_SSU_all.fas ] && echo "Found" || exit
echo "Looking for file: ~/Dropbox/original_sequence_files/LSU_all.fas"
[ -f ~/Dropbox/original_sequence_files/C_LSU_all.fas ] && echo "Found" || exit
echo "Looking for file: ~/Dropbox/original_sequence_files/mtSSU_all.fas"
[ -f ~/Dropbox/original_sequence_files/D_mtSSU_all.fas ] && echo "Found" || exit
echo "Looking for file:  ~/Dropbox/original_sequence_files/MCM7_all.fas"
[ -f ~/Dropbox/original_sequence_files/E_MCM7_all.fas ] && echo "Found" || exit
echo "Looking for file: ~/Dropbox/original_sequence_files/RPB1_all.fas"
[ -f ~/Dropbox/original_sequence_files/F_RPB1_all.fas ] && echo "Found" || exit
echo "Looking for file: ~/Dropbox/original_sequence_files/RPB2_all.fas"
[ -f ~/Dropbox/original_sequence_files/G_RPB2_all.fas ] && echo "Found" || exit
echo "Looking for file: ~/Dropbox/original_sequence_files/ef1a_both_all.fas"
[ -f ~/Dropbox/original_sequence_files/H_ef1a_both_all.fas ] && echo "Found" || exit
echo "Looking for file: IDs_used_for_tree.txt"
[ -f ./IDs_used_for_tree.txt ] && echo "Found" || exit


echo "Reducing files to desired Taxa:"
~/Dropbox/phylo_scripts/reduce.py IDs_used_for_tree.txt ~/Dropbox/original_sequence_files/A_ITS_all.fas > A_ITS_all_red.fas
~/Dropbox/phylo_scripts/reduce.py IDs_used_for_tree.txt ~/Dropbox/original_sequence_files/B_SSU_all.fas > B_SSU_all_red.fas
~/Dropbox/phylo_scripts/reduce.py IDs_used_for_tree.txt ~/Dropbox/original_sequence_files/C_LSU_all.fas > C_LSU_all_red.fas
~/Dropbox/phylo_scripts/reduce.py IDs_used_for_tree.txt ~/Dropbox/original_sequence_files/D_mtSSU_all.fas > D_mtSSU_all_red.fas
~/Dropbox/phylo_scripts/reduce.py IDs_used_for_tree.txt ~/Dropbox/original_sequence_files/E_MCM7_all.fas > E_MCM7_all_red.fas
~/Dropbox/phylo_scripts/reduce.py IDs_used_for_tree.txt ~/Dropbox/original_sequence_files/F_RPB1_all.fas > F_RPB1_all_red.fas
~/Dropbox/phylo_scripts/reduce.py IDs_used_for_tree.txt ~/Dropbox/original_sequence_files/G_RPB2_all.fas > G_RPB2_all_red.fas
~/Dropbox/phylo_scripts/reduce.py IDs_used_for_tree.txt ~/Dropbox/original_sequence_files/H_ef1a_both_all.fas > H_ef1a_both_all_red.fas

echo "Aligning reduced files:"
mafft --genafpair --maxiterate 10000 A_ITS_all_red.fas > A_ITS_all_red_mafft.fas 
mafft --genafpair --maxiterate 10000 B_SSU_all_red.fas > B_SSU_all_red_mafft.fas 
mafft --genafpair --maxiterate 10000 C_LSU_all_red.fas > C_LSU_all_red_mafft.fas
mafft --genafpair --maxiterate 10000 D_mtSSU_all_red.fas > D_mtSSU_all_red_mafft.fas
mafft --globalpair --maxiterate 10000 E_MCM7_all_red.fas > E_MCM7_all_red_mafft.fas  
mafft --globalpair --maxiterate 10000 F_RPB1_all_red.fas > F_RPB1_all_red_mafft.fas
mafft --globalpair --maxiterate 10000 G_RPB2_all_red.fas > G_RPB2_all_red_mafft.fas
mafft --globalpair --maxiterate 10000 H_ef1a_both_all_red.fas > H_ef1a_both_all_red_mafft.fas

echo "Clean up temporary files"
rm A_ITS_all_red.fas
rm B_SSU_all_red.fas
rm C_LSU_all_red.fas
rm D_mtSSU_all_red.fas
rm E_MCM7_all_red.fas
rm F_RPB1_all_red.fas
rm G_RPB2_all_red.fas
rm H_ef1a_both_all_red.fas

echo "Format files for concatenated alignment"
~/Dropbox/phylo_scripts/replace.py A_ITS_all_red_mafft.fas > A_ITS_all_red_mafft_replaced.fas
~/Dropbox/phylo_scripts/replace.py B_SSU_all_red_mafft.fas > B_SSU_all_red_mafft_replaced.fas
~/Dropbox/phylo_scripts/replace.py C_LSU_all_red_mafft.fas > C_LSU_all_red_mafft_replaced.fas
~/Dropbox/phylo_scripts/replace.py D_mtSSU_all_red_mafft.fas > D_mtSSU_all_red_mafft_replaced.fas
~/Dropbox/phylo_scripts/replace.py E_MCM7_all_red_mafft.fas > E_MCM7_all_red_mafft_replaced.fas
~/Dropbox/phylo_scripts/replace.py F_RPB1_all_red_mafft.fas > F_RPB1_all_red_mafft_replaced.fas
~/Dropbox/phylo_scripts/replace.py G_RPB2_all_red_mafft.fas > G_RPB2_all_red_mafft_replaced.fas
~/Dropbox/phylo_scripts/replace.py H_ef1a_both_all_red_mafft.fas > H_ef1a_both_all_red_mafft_replaced.fas

echo "Clean up temporary files"
rm A_ITS_all_red_mafft.fas
rm B_SSU_all_red_mafft.fas
rm C_LSU_all_red_mafft.fas
rm D_mtSSU_all_red_mafft.fas
rm E_MCM7_all_red_mafft.fas
rm F_RPB1_all_red_mafft.fas
rm G_RPB2_all_red_mafft.fas
rm H_ef1a_both_all_red_mafft.fas
rm concat.fas

echo "Create concatenated alignment"
~/Dropbox/phylo_scripts/concat.py IDs_used_for_tree.txt *.fas > concat.fas
echo "Done"