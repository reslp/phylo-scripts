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
		if Sequence[i] is "A": Percent[i] += 1
		if Sequence[i] is "C": Percent[i] += 1
		if Sequence[i] is "G": Percent[i] += 1
		if Sequence[i] is "T": Percent[i] += 1
		if Sequence[i] is "N": Percent[i] += 1

#print len(Percent)
#print len(SequenceList)
#print len (SequenceList[1])
#print MaxSeq
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
	


						
		

