#!/bin/sh

# quick and dirty shell script for combining different scripts to generate concatenated alignments
# also gives overview of the workflow
# written by Philipp Resl 2014

echo "Starting Analysis"

echo "Check if all files are present:"
echo "Looking for file: raw/ITS_all.fas"
[ -f raw/ITS_all.fas ] && echo "Found raw/ITS_all.fas" || exit
echo "Looking for file: raw/SSU_all.fas"
[ -f raw/SSU_all.fas ] && echo "Found" || exit
echo "Looking for file: raw/LSU_all.fas"
[ -f raw/LSU_all.fas ] && echo "Found" || exit
echo "Looking for file: raw/mtSSU_all.fas"
[ -f raw/mtSSU_all.fas ] && echo "Found" || exit
echo "Looking for file:  raw/MCM7_all.fas"
[ -f raw/MCM7_all.fas ] && echo "Found" || exit
echo "Looking for file: raw/RPB1_all.fas"
[ -f raw/RPB1_all.fas ] && echo "Found" || exit
echo "Looking for file: raw/RPB2_all.fas"
[ -f raw/RPB2_all.fas ] && echo "Found" || exit
echo "Looking for file: raw/ef1a_both_all.fas"
[ -f raw/ef1a_both_all.fas ] && echo "Found" || exit
echo "Looking for file: names.txt"
[ -f ./names.txt ] && echo "Found" || exit


echo "Reducing files to desired Taxa:"
reduce.py names.txt raw/ITS_all.fas > A_ITS_all_red.fas
reduce.py names.txt raw/SSU_all.fas > B_SSU_all_red.fas
reduce.py names.txt raw/LSU_all.fas > C_LSU_all_red.fas
reduce.py names.txt raw/mtSSU_all.fas > D_mtSSU_all_red.fas
reduce.py names.txt raw/MCM7_all.fas > E_MCM7_all_red.fas
reduce.py names.txt raw/RPB1_all.fas > F_RPB1_all_red.fas
reduce.py names.txt raw/RPB2_all.fas > G_RPB2_all_red.fas
reduce.py names.txt raw/ef1a_both_all.fas > H_ef1a_both_all_red.fas

echo "Aligning reduced files:"
# mafft is needed here.
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
replace.py A_ITS_all_red_mafft.fas > A_ITS_all_red_mafft_replaced.fas
replace.py B_SSU_all_red_mafft.fas > B_SSU_all_red_mafft_replaced.fas
replace.py C_LSU_all_red_mafft.fas > C_LSU_all_red_mafft_replaced.fas
replace.py D_mtSSU_all_red_mafft.fas > D_mtSSU_all_red_mafft_replaced.fas
replace.py E_MCM7_all_red_mafft.fas > E_MCM7_all_red_mafft_replaced.fas
replace.py F_RPB1_all_red_mafft.fas > F_RPB1_all_red_mafft_replaced.fas
replace.py G_RPB2_all_red_mafft.fas > G_RPB2_all_red_mafft_replaced.fas
replace.py H_ef1a_both_all_red_mafft.fas > H_ef1a_both_all_red_mafft_replaced.fas

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
concat.py names.txt *.fas > concat.fas
echo "Done"