#!/usr/bin/env python
# script calculates percentage of available bases for each position in alignment
import sys

Info = """
Send me an infile!
"""

#if len(sys.argv) != 2:
#	sys.stderr.write(Info)
#	quit()
#else:
#	FileName = sys.argv[1]
FileName =  "concat.fas" 

TaxonList = []
SequenceList = []

File = open(FileName, "U")

for Line in File:
	if Line[0] == ">":
		TaxonList.append(Line)
	else:
		SequenceList.append(Line)

MaxSeq = len(TaxonList)
#print MaxSeq
Percent = [0.0]*len(SequenceList[1])
#print SequenceList
for Sequence in SequenceList:
	Sequence.replace("\n", "")
	for i in range(len(Sequence)):
		if Sequence[i] is "A": Percent[i] += 1
		if Sequence[i] is "C": Percent[i] += 1
		if Sequence[i] is "G": Percent[i] += 1
		if Sequence[i] is "T": Percent[i] += 1

Number = 0
for Element in Percent:
	Percent[Number] = ((Element*100)/MaxSeq)
	print Number,  " %.2f" % Percent[Number]
	Number += 1
		

File.close()
