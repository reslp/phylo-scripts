#!/usr/bin/env python
# this scripts splits FASTA alignments in codon positions
# usage: split_codons.py <file.fas>
# output: 3 files with the same name as the input file + Pos1,2,3 for the separate codons
# written by Philipp Resl, last change: Feb 07, 2015


import sys

if len(sys.argv) < 2:
	print "Please provide correct input. usage: split_codons.py <file.fas> "
	quit()
else:
 	AlignmentFileName = sys.argv[1]
AlignmentFile = open(AlignmentFileName, "U")

#get list of taxa
TaxonList = []
for Line in AlignmentFile:
	if Line[0] == ">":
		TaxonList.append(Line)

#create sequence lists
MaxSeq = len(TaxonList)
SequenceList = [""] * MaxSeq
AlignmentFile.seek(0)
SeqNum = -1
for Line in AlignmentFile:
	if Line[0] != ">":
		SequenceList[SeqNum] += Line
	else:
		SeqNum += 1
AlignmentFile.close()

SeqNumber = 0

for Single in SequenceList:
	SequenceList[SeqNumber] = Single.replace("\n", "")
	TaxonList[SeqNumber] = TaxonList[SeqNumber].replace("\n","")
	SeqNumber += 1	

Pos_1 = [""]* MaxSeq
Pos_2 = [""]* MaxSeq
Pos_3 = [""]* MaxSeq
SeqNumber = 0

for Sequence in SequenceList:
	i = 0
	while (i <= len(Sequence)-3):
		Pos_1[SeqNumber] += Sequence[i]
		Pos_2[SeqNumber] += Sequence[i+1]
		Pos_3[SeqNumber] += Sequence[i+2]
		i += 3
	if (len(Sequence)-i) == 2:
		Pos_1[SeqNumber] += Sequence[i]
		Pos_2[SeqNumber] += Sequence[i+1]
	if (len(Sequence)-i) == 1:
		Pos_1[SeqNumber] += Sequence[i]
	SeqNumber +=1
	
#output:
AlignmentFileName = AlignmentFileName.replace(".fas","")
Pos1_file = open(AlignmentFileName + "_pos1.fas", "w")
Pos2_file = open(AlignmentFileName + "_pos2.fas", "w")
Pos3_file = open(AlignmentFileName + "_pos3.fas", "w")

for index, Taxon in enumerate(TaxonList):
	Pos1_file.write(Taxon + "_Pos1"+"\n")
	Pos1_file.write(Pos_1[index]+"\n")
	
	Pos2_file.write(Taxon + "_Pos2"+"\n")
	Pos2_file.write(Pos_2[index]+"\n")
	
	Pos3_file.write(Taxon + "_Pos3"+"\n")
	Pos3_file.write(Pos_3[index]+"\n")

Pos1_file.close()
Pos2_file.close()
Pos3_file.close()
