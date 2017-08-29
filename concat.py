#!/usr/bin/env python
# Concatenator script to create concatenated alignments for multiple loci
# written by Philipp Resl, Okt. 2013
# code may be freely distributed and modified
# feedback to: philipp.resl@uni-graz.at
# http://resl.tumblr.com
# last change: 29.08.2017

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

sys.stderr.write("(concat.py) Starting concatenation\n")

#reading Taxa from taxonfile
TaxonFile = open(TaxonFilename, "U")
TaxonList = []
for Line in TaxonFile:
	TaxonList.append(Line.strip("\n"))
	
for element in set(TaxonList):
	if TaxonList.count(element) > 1:
		sys.stderr.write("(concat.py) Possible Problem: Duplicated Taxon in Taxon list: %s \n" % (element.strip()))


TaxonListOutput = TaxonList [:] #Taxon List for Output
TaxonFile.close()

#output filelist
sys.stderr.write("(concat.py) Will use the following files:\n")
for InfileName in FileList:
	sys.stderr.write("(concat.py) "+ InfileName + "\n")
	
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

i=0
for file in FileList:
	File = open(file, "U")
	full_file = File.read()
	for Taxon in TaxonList:
		if full_file.count(">"+Taxon) > 1:
			sys.stderr.write("(reduce.py) Possible Problem with %s: Sequence ID %s is not unique in the sequence file.\n" % (file,Taxon))
	if ">" not in full_file:
		sys.stderr.write("(concat.py) Possible Problem with %s: No sequences found. Is the file not in FASTA format or is the file empty?\n" % (file))
	File.close()

#search for sequence in file
i = 0
Found = 0
for i in range(0, len(FileList)):
	Sequenzfile = open(FileList[i], "U")
	sys.stderr.write("(concat.py) Processing: "+FileList[i]+"\n")
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
	Sequenzfile.close()
	SequenceList = add_missing(SequenceList)

# print Output:
for i in range(0, TotTax):
	print ">" + TaxonListOutput[i]
	print SequenceList[i]

sys.stderr.write("(concat.py) Your file is ready.\n")
	
