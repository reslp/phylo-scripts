#!/usr/bin/env python
# Concatenator script to create concatenated alignments for multiple loci
# written by Philipp Resl, Okt. 2013
# code may be freely distributed and modified
# feedback to: philipp.resl@uni-graz.at
# http://resl.tumblr.com
# last change: 02.04.2014

import sys #for command line arguments

#print "Concatenator"
Info = """
Hi.

I will create a concatenated alignment file out of multiple alignment files.
I use a reference file with a list of taxa and will arrange the sequences
accordingly. I will only consider taxa included in taxon list!
ALL INPUT FILES HAVE TO BE UNIX ENCODED
Output will look like (for Sample A534 in a 3 locus alignment with 2nd locus 
missing):

>A534X_X ??AGTCGTCGCGTNNNNNNNNNN?????????????NNNNNNNNNN???ACGT--GCG???
>A535XX_ ACAGTGGACG???NNNNNNNNNNAGCGTCGCGCTGCNNNNNNNNNN???????????????
^	    [locus1]     [spacer]  [locus2]     [spacer]   [locus3]
[Sequencename with locus availability attached]

usage:
concat.py <taxonlist file> <inputfile1> <inputfile2> > <outputfile>

examples:
concat.py taxalist.txt alignment1.fas alignment2.fas ... > myalignment.fas
or
concat.py list_names.txt *.fas > output.fas
"""

if len(sys.argv) < 2:
	print Info
	quit()
else:
 	TaxonFilename = sys.argv[1]
 	FileList = sys.argv[2:]

sys.stderr.write("\nStarting...")
#reading Taxa from taxonfile
TaxonFile = open(TaxonFilename, "r")
TaxonList = []
for Line in TaxonFile:
	TaxonList.append(Line.strip("\n"))
#sys.stderr.write("List of Taxa:\n %s\n" % TaxonList)
TaxonListOutput = TaxonList [:] #Taxon List for Output
TaxonFile.close()

#output filelist
sys.stderr.write("\nI will use the following files:\n")
for InfileName in FileList:
	sys.stderr.write(InfileName + "\n")
	
#get total number of taxa
TotTax = len(TaxonList)

#create a blank Sequencelist for given number of taxa
SequenceList = [""]*len(TaxonList)

TaxonNum = 0
LineIndex = 0
LineNum = 0

def add_missing(SList):
	Index = 0
	LongestItem = max(SList, key=len)
	for Item in SList:
		if len(Item) <= len(LongestItem):
			SList[Index] += "?" * (len(LongestItem) - len(Item))
			SList[Index] += "N" * 30
		Index += 1
	return SList
# end of add_missing()

def add_to_taxon(WhichTaxon):
	TaxonListOutput[WhichTaxon] += "O"
	return
# end of add_to_taxon
	
#search for sequence in file
i = 0
for i in range(0, len(FileList)):
	Sequenzfile = open(FileList[i], "r")
	sys.stderr.write("\nOpening:\n"+FileList[i])
	TaxonNum = 0
	for Element in TaxonList:
		for Line in Sequenzfile:
			Found = 0
			if Element in Line:
				SequenceList[TaxonNum] += Sequenzfile.next().strip("\n")
				TaxonListOutput[TaxonNum] += "X"
				Found = 1
				break				
			LineIndex += 1	
		if Found == 0:
			add_to_taxon(TaxonNum)
		LineIndex = 0
		Sequenzfile.seek(0)	
		TaxonNum +=1
	SequenceList = add_missing(SequenceList)

# print Output:
for i in range(0, TotTax):
	print ">" + TaxonListOutput[i]
	print SequenceList[i]

sys.stderr.write("\nYour file is ready.\n")
	
