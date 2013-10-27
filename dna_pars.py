#!/usr/bin/env python

# script loads alignment in fasta format from BioEdit and replaces - with ?
# line endings must be MS Windows encoded as in Bioedit saved files!
# output file will be unix encoded!
# Version1, changed: 15.10.2013

import os

print """
FASTA FILE PARSER V1\n
This Script takes a BioEdit (Windows encoded) FASTA file as input and replaces
gaps (-) from the beginning and end of the file.It also converts the file to a Unix
encoded file.An Output file named <inputfilename>_parsed will be generated.
Filename has to be entered with a leading slash."""

WD = os.getcwd() # get working directory
#print WD

Infilename = WD + "/"
Infilename += raw_input("Enter Filename e.g. example.fas, folder/example2.fas: ")
Outfilename = Infilename + "_parsed"

#Infilename = "ITS_all_muscle.fas"
#Outfilename = "out.fas"

#print Infilename

Infile = open(Infilename, "r")
Outfile = open(Outfilename, "w")

Linenumber = 0

#count number of taxa
Ntax = 0
for Line in Infile:
	if Line[0] == ">":
		Ntax +=1

TaxonName = []
Sequenzen = [None]*Ntax
TaxonNumber = -1
Line2 = ""

Infile.seek(0) #reset read curser in file to begin

for Line in Infile:
	if Line[0] == ">":
		Line2 = ""
		TaxonNumber += 1
		Line = Line.strip("\n").strip("\r")
		TaxonName.append(Line)
	else: # when line is a sequence
		Line2 += Line.strip("\n").strip("\r")
		Sequenzen[TaxonNumber] = Line2
		#print TaxonNumber
	Linenumber += 1	

#print TaxonName
#print Sequenzen
#print "Taxa: ", len(TaxonName)
#print "Seqs: ", len(Sequenzen)

#Sequenz_0 = list(Sequenzen[1])

whichSeq = 0
for Sequenz in Sequenzen:
	Sequenz_0 = list(Sequenzen[whichSeq])
	zahl = 0

#replace all - from the beginning fo sequence	
	for Base in Sequenz_0:
		if Base == "-":
			Sequenz_0[zahl] = "?"
		else:
			break
		zahl += 1

#replace all - from the end of the sequence
	zahl2 = -1
	for Base in Sequenz_0:
		if Sequenz_0[len(Sequenz_0) + zahl2] == "-":
			Sequenz_0[len(Sequenz_0) + zahl2] = "?"	
		else:
			break
		#print zahl
		zahl2 -= 1
	Sequenzen[whichSeq] = "".join(Sequenz_0)		
	whichSeq += 1

# write labels and worked seqs to file
which_tax = 0
for Taxon in TaxonName:
	Outfile.write(Taxon + "\n")
	Outfile.write(Sequenzen[which_tax]+ "\n")
	which_tax += 1

#print Sequenzen
#print TaxonName
#print Sequenzen
#print "Taxa: ", len(TaxonName)
#print "Seqs: ", len(Sequenzen)

print "I found %d taxa with %d sequences. The Output was written to: \n%s" % (len(TaxonName), len(Sequenzen), Outfilename)

Infile.close()
Outfile.close()

