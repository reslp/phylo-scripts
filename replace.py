#!/usr/bin/env python
# script replaces - with ? at the beginning and end of textfile
# written by Philipp Resl, Dec. 2013
# code may be freely distributed and modified
# feedback to: philipp.resl@uni-graz.at
# http://philipp.resl.xyz
# modified: 29.08.2017

import sys

Info = """
replace.py: Replaces - with ? at the beginning and end of fasta alignments
Usage: replace.py input.fas > output.fas
"""

if len(sys.argv) != 2:
	sys.stderr.write(Info)
	quit()
else:
	FileName = sys.argv[1]

def replace_begin (Sequenz_0):
	zahl = 0
	for Base in Sequenz_0:
		if Base == "-":
			Sequenz_0[zahl] = "?"
		else:
			break
		zahl += 1
	return "".join(Sequenz_0)
# end replace_begin

#replace all - from the end of the sequence
def replace_end (Sequenz_0):
	zahl2 = -1
	for Base in Sequenz_0:
		if Sequenz_0[len(Sequenz_0) + zahl2] == "-":
			Sequenz_0[len(Sequenz_0) + zahl2] = "?"	
		else:
			break
		zahl2 -= 1
	return "".join(Sequenz_0)
#end replace_end

TaxonList = []
File = open(FileName, "U")
file = File.read()
if ">" not in file:
		sys.stderr.write("(replace.py) Possible Problem: No sequences found. This the file not in FASTA format or is the file empty?\n")

File.seek(0)
for Line in File:
	if Line[0] == ">":
		TaxonList.append(Line)
for element in set(TaxonList):
	if TaxonList.count(element) > 1:
		sys.stderr.write("(replace.py) Possible Problem: Duplicated Sequence: %s \n" % (element.strip()))
		
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
	SequenceList[SeqNumber] = replace_begin(list(SequenceList[SeqNumber]))
	SequenceList[SeqNumber] = replace_end(list(SequenceList[SeqNumber]))
	TaxonList[SeqNumber] = TaxonList[SeqNumber].replace("\n","")
	SeqNumber += 1


for Taxon in range(0,MaxSeq):
	print TaxonList[Taxon]
	print SequenceList[Taxon]
	

File.close()
	


						
		

