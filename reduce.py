#!/usr/bin/env python
# Reduces Alignment to selected sequences
# written by Philipp Resl, Dec. 2013
# code may be freely distributed and modified
# feedback to: philipp.resl@uni-graz.at
# http://resl.tumblr.com
# modified: 18.08.14
import sys #for command line arguments

Info = """
wrong arguments provided...

"""

if len(sys.argv) < 2:
	print Info
	quit()
else:
 	TaxonFilename = sys.argv[1]
 	File = sys.argv[2]

#reading Taxa from taxonfile
TaxonFile = open(TaxonFilename, "r")
TaxonList = []

for Line in TaxonFile:
	if "\r\n" in Line: #probably not needed, only for windows
		TaxonList.append(Line.strip("\r\n"))
	else:
		TaxonList.append(Line.strip("\n"))
	
#sys.stderr.write("Reducing file %s to this list of Taxa:\n %s\n" % (File, TaxonList))
TaxonListOutput = TaxonList [:] #Taxon List for Output
TaxonFile.close()

#get total number of taxa
TotTax = len(TaxonList)

#create a blank Sequencelist for given number of taxa
SequenceList = [""]*len(TaxonList)
#print SequenceList

Sequenzfile = open(File, "U")
#Open and read Files

Found = 0
for Taxon in TaxonList:
	for Line in Sequenzfile:
		#print Taxon
		#print Line
		if Line.startswith(">"+Taxon):
			print Line.strip("\n")
			Found = 1
			continue
		if Found == 1:
			if Line.find(">") == -1:
				print Line.strip("\n")
			else:
				Found = 0
	Sequenzfile.seek(0)
			
	
			
		
	
		

	
