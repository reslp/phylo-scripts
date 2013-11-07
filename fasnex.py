#!/usr/bin/env python
import sys

Info = """Fasta to nexus converter. Version 1\n\n
Usage: fasnex.py input.fas > output.nex
"""

if len(sys.argv) < 2:
	sys.stderr.write(Info)
	quit()
else:
 	Fastafilename = sys.argv[1]
 	
Fastafile = open(Fastafilename, "U")
TaxonList = []

# Get names of Taxa
for Line in Fastafile:
	if Line[0] == ">":
		NewLine = Line.replace(">","")
		TaxonList.append(NewLine.strip("\n"))

WhichSeq = -1
TaxNumber = len(TaxonList)
SequenceList = [""] * TaxNumber
Fastafile.seek(0)
TaxCount = 0

#Get Sequences
for Line in Fastafile:
	if Line[0] != ">":
		SequenceList[WhichSeq] += Line.strip("\n")
	else:
		WhichSeq += 1	
		
LongestSeq = max(SequenceList, key=len)
print "#NEXUS\n"
print "BEGIN data;\n"
print "Dimensions: ntax=%d nchar=%d;\n" % (TaxNumber, len(LongestSeq))
print "Format datatype=dna missing=? gap=-;\n"
print "Matrix\n"
WhichSeq = 0

for Taxon in TaxonList:
	print Taxon, "\t", SequenceList[WhichSeq]
	WhichSeq += 1
print ";\n"
print "END;\n"	


Fastafile.close()
