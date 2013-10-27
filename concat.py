#!/usr/bin/env python
# Concatenator script to create concatenated alignments for multiple loci
# written by Philipp Resl, Okt. 2013
# code may be freely distributed and modified
# feedback to: philipp.resl@uni-graz.at
# http://resl.tumblr.com
import sys #for command line arguments

#print "Concatenator"
Info = """
CONCATENATOR 1.0

Concatenator creates a concatenated alignment file out of multiple alignments.
It uses a reference file with a list of taxa and will arrange the sequences
accordingly. It will only consider taxa included in taxon list!
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

#TaxonFilename = "names.txt"
#FileList = ["align1_ITS.fas","align2_MCM7.fas","align3_RPB.fas"]
#TaxonFilename = "test_names.txt"
#FileList = ["ITS.fas","SSU.fas"]

#reading Taxa from taxonfile
TaxonFile = open(TaxonFilename, "r")
TaxonList = []
for Line in TaxonFile:
	TaxonList.append(Line.strip("\n"))
sys.stderr.write("List of Taxa:\n %s\n" % TaxonList)
TaxonListOutput = TaxonList [:] #Taxon List for Output
TaxonFile.close()

for InfileName in FileList:
	sys.stderr.write("Using file: %s\n" % InfileName)
	
#get total number of taxa
TotTax = len(TaxonList)

#create a blank Sequencelist for given number of taxa
SequenceList = [""]*len(TaxonList)
#print SequenceList

#Sequenzfile = open(FileList[2], "r")
#Open and read Files
TaxonNum = 0
LineIndex = 0
LineNum = 0

def add_missing(SList):
	Index = 0
	#print "Adding missing Sequences to List"
	LongestItem = max(SList, key=len)
	for Item in SList:
		if len(Item) < len(LongestItem):

			SList[Index] += "?" * (len(LongestItem) - len(Item))

		Index += 1
	return SList
# end of add_missing()

def add_to_taxon(WhichTaxon):
	TaxonListOutput[WhichTaxon] += "O"
	return
# end of add_to_taxon
	
#search for sequence in file
i = 0
#Found = 0
for i in range(0, len(FileList)):
	Sequenzfile = open(FileList[i], "r")
	TaxonNum = 0
	#print "Filenumber: ", i
	for Element in TaxonList:
		#print Element
		for Line in Sequenzfile:
			Found = 0
			if Element in Line:
				try:
					if i==0: # avoid NNNNN at the beginning of sequence
						SequenceList[TaxonNum] += Sequenzfile.next().strip("\n")
						TaxonListOutput[TaxonNum] += "X"
						Found = 1
						break
					else:
						SequenceList[TaxonNum] += ("N" * 30 + Sequenzfile.next().strip("\n"))
						#print "Found %s in %s in line %d" % (Element, Line, LineIndex)
						TaxonListOutput[TaxonNum] += "X"
						Found = 1
						break
				except StopIteration: #when sequence for taxon is not found
					#insert ????? with the length of sequence
					sys.stderr.write("Fehler")		
			LineIndex += 1	
		
		if Found == 0:
			add_to_taxon(TaxonNum)
		#print Found
		LineIndex = 0
		Sequenzfile.seek(0)	
		TaxonNum +=1
	SequenceList = add_missing(SequenceList)

# print Output:
for i in range(0, TotTax):
	print ">" + TaxonListOutput[i]
	print SequenceList[i]

sys.stderr.write("Done")
	
