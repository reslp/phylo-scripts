phylo-scripts
=========

This repository contains several small scripts that help with creating concatenated sequences alignments from multiple single locus files.
I created these scripts to be able to quickly create alignments with different taxon samplings for phylogenetic reconstructions.


Description
===========

The pipeline takes single locus files as input and creates a concatenated alignment file according to a desired taxon set.


How does it work?
================

 `get_analysis.sh` is the master script that controls the pipeline. First it checks if all the mandatory files are present. Then it reduces the provided FASTA files to the desired set of taxa by calling the script `reduce.py`. The set of taxa is contained in the file: `IDs_used_for_tree.txt` (see below). Now, `mafft`is called to align the reduced single locus files. Next, gaps (-) that were introduced by mafft at the beginning and end of the alignments are replaced by question marks (?). Finally, 
`concat.py` combines the aligned single locus files into one single file and adds question marks for missing loci.

You will end up with a file called concat.fas that contains a concatenated alignment for all the taxa provied in your ID file.

Also you may have a look at the `PIPELINE_USAGE.txt` file

Requirements and installation
============

- MacOS X or other Unix like operating system (Windows Version in the works)
- [python](www.python.org) 2.7.8+, which comes with most Unix like systems
- [mafft](http://mafft.cbrc.jp/alignment/software/) v7, for the alignment function


1. Download repository
2. Make sure mafft is in your PATH
3. Modify scripts to match your own analysis
4. run get_analysis.sh


How do I modify the scripts for my own dataset?
========
Several parts of the pipeline are personalized for my own needs. However, it is easy to adapt them for your own analyses.
Normally the only script you have to edit is `get_analysis.sh` to match the path and number of your single locus files. Open the file in a normal text editor and change the file paths according to the situation on your computer. 

All scripts take absolute and relative paths as input. Because all temporary files will be crreated in the same directory your scripts run in, I recommend to use absolute paths for the `reduce.py` script and keep your original single locus files in a seperate directory, so that you don't accidentaly delete your raw data files. You can also change the alignment algorithm `mafft`uses. Just change the settings according to your needs.

Please also have a look at the PIPELINE_USAGE.txt file. If you have any further questions, feel free to contact me.

What does the file IDs_used_for_tree.txt do?
=========
This "IDs_used_for_tree.txt" tells the pipeline which taxa you would like to include in your concatenated alignment. It includes names that the scripts search for in your single locus files. The important part is that the sequences in your single locus files also start with those identifiers.

An example:
Say in your ID file you have the name X132. The scripts will search for sequences that start with this name in your FASTA files.
Valid names would be: >X132_Temella_sp or >X132_unknown_algae. The scripts will not recognise sequences with names like: >_new_seq_X132 or >mtssu_X132_old
Also make sure that the names provided in your ID file are unique.
The rational behind this is that by providing a unique name for taxa/extractions the script will know which sequences from different loci belong to this taxon.

What do the other scripts do?
=========
There are several other scripts included in the package:

`fasnex.py` is a simple FASTA to NEXUS file converter. Usage: `./fasnex.py input.fas > output.nex`

`name_tree.py` is a script to put readable names on the tree after using concat. Usage: `./name_tree.py tree_names.txt input_tree.tre > output_tree.tre`. Important: tree_names.txt has to be tab delimited with the first column containing the IDs from your IDs_used_for_tree.txt file and the second column containing the desired readable names.

`pcrop.py` crops your FASTA alignment to positions with a given minimum percentage of nucleotides relative to all taxa in the alignment. Usage: Usage: `./pcrop.py <cutoff%> <inputfile> > <outputfile>`


Usage
=======
Simply execute:
`./get_analysis.sh`

How do I cite this?
=========
When you use these scripts please add these two citations to your manuscript:

Philipp Resl (2015): phylo-scripts: Python scripts for phylogenetics. release v0.1. available at: http://github.com/reslp [![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.15983.svg)](http://dx.doi.org/10.5281/zenodo.15983)

Philipp Resl, Kevin Schneider, Martin Westberg, Christian Printzen, Zdeněk Palice, Göran Thor, Alan Fryday, Helmut Mayrhofer and Toby Spribille (2015) Diagnostics for a troubled backbone: testing topological hypotheses of trapelioid lichenized fungi in a large-scale phylogeny of Ostropomycetidae (Lecanoromycetes). Fungal Diversity (in press)


COPYRIGTH AND LICENSE
=====================

Copyright (C) 2014 Philipp Resl

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program in the file LICENSE. If not, see http://www.gnu.org/licenses/.




