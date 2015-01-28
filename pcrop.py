#!/usr/bin/env python
# script calculates percentage of available bases for each position in alignment
# and cuts of every base below a specified value.

import sys
Info = """
Usage: pcrop.py <cutoff%> <inputfile> > <outputfile>
"""
if len(sys.argv) <= 2:
	sys.stderr.write(Info)
	quit()
else:
	CutOff = int(sys.argv[1])
	FileName = sys.argv[2]
	
#FileName =  "concat.fas" 
TaxonList = []
SequenceList = []

File = open(FileName, "U")

for Line in File:
	if Line[0] == ">":
		TaxonList.append(Line)
	else:
		SequenceList.append(Line)

MaxSeq = len(TaxonList)

Percent = [0.0]*len(SequenceList[1])

for Sequence in SequenceList:
	Sequence.replace("\n", "")
	for i in range(len(Sequence)):
		if Sequence[i] in "ACGTN": Percent[i] += 1

Number = 0
index = 0
RedSequence  = [""] * MaxSeq

for Sequence in SequenceList:
	WorkSeq = list(Sequence)
	#print WorkSeq
	for Element in Percent:
		if (Element*100/MaxSeq > CutOff):
			RedSequence[Number] += WorkSeq[index]
		index += 1	
	index = 0
	Number += 1

for i in range(0,MaxSeq):
	print TaxonList[i], RedSequence[i]

File.close()
	


						
		

