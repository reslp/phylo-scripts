#!/usr/bin/env python
# script replaces - with ? at the beginning and end of textfile
# Version3, changed: 07.11.2013

import sys

Info = """
Single_Line: creates fasta files with sequences in single lines
"""

if len(sys.argv) != 2:
	sys.stderr.write(Info)
	quit()
else:
	FileName = sys.argv[1]


TaxonList = []

File = open(FileName, "U")
for Line in File:
	if Line[0] == ">":
		TaxonList.append(Line)

MaxSeq = len(TaxonList)
SequenceList = [""] * MaxSeq
File.seek(0)
SeqNumber = -1	
for Line in File:
	if Line[0] != ">":
		SequenceList[SeqNumber] += Line
	else:
		SeqNumber += 1

SeqNumber = 0
for Single in SequenceList:
	SequenceList[SeqNumber] = Single.replace("\n", "")
	#SequenceList[SeqNumber] = replace_begin(list(SequenceList[SeqNumber]))
	#SequenceList[SeqNumber] = replace_end(list(SequenceList[SeqNumber]))
	TaxonList[SeqNumber] = TaxonList[SeqNumber].replace("\n","")
	SeqNumber += 1


for Taxon in range(0,MaxSeq):
	print TaxonList[Taxon]
	print SequenceList[Taxon]
	

File.close()
	


						
		

