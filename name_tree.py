#! /usr/bin/python

import sys
import csv

usage = """
Makes a tree with cryptic taxon names readable:

Usage: name_tree.py <namelistfile> <treefile> > <output.tre>

treefile has to be NEXUS or NEWICK format
namelistfile has to be tab delimited file with name which has to be replaced in
the first column and the more readable name in the second column.
"""

if len(sys.argv) < 3:
	print usage
	quit()
else:
 	NamesFileName = sys.argv[1]
 	TreeFileName = sys.argv[2]

NamesFile = open(NamesFileName, "r")
TreeFile = open(TreeFileName, "r")

NamesList = []
i = 0
for Line in NamesFile:
	Line = Line.strip("\n")
	fields = Line.split("\t")
	NamesList.append(fields)
	i+=1

for Line in TreeFile:
	for j in range(1,i):
		Replacer = NamesList[j][0] + NamesList[j][1] # alter for namen scheme
		Line = Line.replace(NamesList[j][0], Replacer)

print Line
	
NamesFile.close()
TreeFile.close()