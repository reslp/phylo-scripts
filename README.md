phylo-scripts
=========

This repository contains several small scripts that help with creating concatenated sequences alignments from multiple single locus files.
I created these scripts to be able to quickly create alignments with different taxon samplings for phylogenetic reconstructions.


DESCRIPTION
===========

The pipeline takes single locus files as input and creates a concatenated alignment file according to a desired taxon set.


How does it work?
================

The master script that controls the pipeline is the bash script `get_analysis.sh`. First this script checks if all the mandatory files are present. Then it reduces the provided files to the desired set of taxa by calling the script `reduce.py`. The set of taxa is contained in the file: `IDs_used_for_tree.txt`. Now, `mafft`is called to align the reduced single locus files. Next, gaps (-) that were introduced by mafft at the beginning and end of the alignments are replaced by question marks (?). Finally, 
`concat.py` combines the aligned single locus files into one single file and adds question marks for missing loci.


REQUIREMENTS
============

- MacOS X or other Unix like operating system (Windows Version in the works)
- [python](www.python.org) 2.7.8+, which comes with most Unix like systems
- [mafft](http://mafft.cbrc.jp/alignment/software/) v7, for the alignment function


EXAMPLES
========

probably the simplest way to call concat.py is to provide a sequence ID file and a directory containing FASTA files of individual loci:

`python concat.py -t SeqIDFile.txt -d /path/to/sequences/ `

Getting help (displays all available command options):

`python concat.py -h`



COPYRIGTH AND LICENSE
=====================

Copyright (C) 2014 Philipp Resl

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program in the file LICENSE. If not, see http://www.gnu.org/licenses/.




See PIPELINE_USAGE.txt from information on how this works.
