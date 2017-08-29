#!/usr/bin/env python
# Reduces Alignment to selected sequences
# written by Philipp Resl, Dec. 2013
# code may be freely distributed and modified
# feedback to: philipp.resl@uni-graz.at
# http://philipp.resl.xyz
# modified: 29.08.2017
import sys #for command line arguments

Info = """
reduce.py
Usage: reduce.py <namelistfile.txt> <input_alignmentfile> > <outputfile>
"""

if len(sys.argv) < 2:
	print Info
	quit()
else:
 	TaxonFilename = sys.argv[1]
 	File = sys.argv[2]

#reading Taxa from taxonfile
TaxonFile = open(TaxonFilename, "U")
TaxonList = []

for Line in TaxonFile:
	if "\r\n" in Line: #probably not needed since the file is opened with universal mode, only for windows
		TaxonList.append(Line.strip("\r\n"))
	else:
		TaxonList.append(Line.strip("\n"))
TaxonFile.close()

for element in set(TaxonList):
	if TaxonList.count(element) > 1:
		sys.stderr.write("(reduce.py) Possible Problem: Duplicated Taxon in Taxon list: %s \n" % (element.strip()))

	
#sys.stderr.write("Reducing file %s to this list of Taxa:\n %s\n" % (File, TaxonList))
TaxonListOutput = TaxonList [:] #Taxon List for Output


#get total number of taxa
TotTax = len(TaxonList)

#create a blank Sequencelist for given number of taxa
SequenceList = [""]*len(TaxonList)

Sequenzfile = open(File, "U")
#Open and read Files and perform some basic checks
file = Sequenzfile.read()
for Taxon in TaxonList:
	if file.count(">"+Taxon) > 1:
		sys.stderr.write("(reduce.py) Possible Problem with %s: Sequence ID %s is not unique in the sequence file.\n" % (File, Taxon))
if ">" not in file:
		sys.stderr.write("(reduce.py) Possible Problem with %s: No sequences found. Is the file not in FASTA format or is the file empty?\n" % (File))



Found = 0
for Taxon in TaxonList:
	for Line in Sequenzfile:
		if Line.startswith(">"+Taxon): #sequence name has to start with Taxon ID
			print Line.strip("\n")
			Found = 1
			continue
		if Found == 1:
			if Line.find(">") == -1:
				print Line.strip("\n")
			else:
				Found = 0
	Sequenzfile.seek(0)
			
	
			
		
	
		

	
