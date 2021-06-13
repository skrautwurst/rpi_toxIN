#!/usr/bin/env python3

"""

Extract information (database accession ID and name) from various result files (cmsearch, hmmsearch, database entries). Saves output file in csv format and includes accession ID and name description.

Usage:
    extract_id-species.py [options] <INFILE> <OUTPUTFILE>

Options:
    -h, --help                                  Show this help message and exit.
    -t TOOLTYPE, --tooltype TOOLTYPE            Tool or database or source, from which the input INFILE was generated. Implemented options: rfam, pdb, pfam, cmsearch, hmmsearch, literature1, literature2 [default: rfam]

Dependencies:
    BioPython 1.73 or greater
    docopt 0.6.2 or greater

"""

###################################

import csv
import sys

from Bio import Entrez
from Bio import ExPASy
from Bio import SwissProt
from Bio import SeqIO
from docopt import docopt

###################################

Entrez.email = "sarah.krautwurst@uni-jena.de"

def get_name(id):  # get organism name of an UniProt ID (necessary for Pfam entries)
    """
    Get the species name for an UniProt ID.

    Parameters:
    id -- UniProt ID

    Return:
    species name

    """

    while 1:
        try:
            handle = ExPASy.get_sprot_raw(id)
            record = SwissProt.read(handle)
            handle.close()
            #print(f"Entry {id} found.")
            return record.organism[:-1].replace(" ","_") #exclude point at the end of organism line, replace spaces
        except RuntimeError:
            time.sleep(5)
            continue
        except ValueError:
            print(f"No record found for ID {id}\n")
            continue
        break


###################################

if __name__ == '__main__':
    """
    Main method.
    """
    ###################################
    # argument parsing
    args = docopt(__doc__)

    file = args['<INFILE>']
    outfile = args['<OUTPUTFILE>']
    toolType = args['--tooltype']

    ###################################
    # variable declaration
    inputTable = {}
    info = {}  # dictionary: keys are accession IDs, value are corresponding species name

    ###################################
    # read input IDFILE
    if toolType=='cmsearch' or toolType=='hmmsearch': # input files are tabular with header/comment lines
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=' ') # tables are space/tab-delimited
            for row in csv_reader:
                if row:
                    if row[0].startswith('#'): # files have multiple comment lines at the top and bottom, these are excluded here
                        continue
                    else:
                        key = row[0] # accession ID
                        values = []
                        for item in row[1:]:
                            if item !="":
                                values.append(item) # store content of all columns of input file, gets rid of the spaces and tabs between columns
                            else:
                                continue
                        inputTable[key] = values
                        # contains less entries than in input file because for some accession IDs multiple matches were present in input file (only once stored here)

                        #print(key)
                        #print(values)

    else: # for literature, pdb, rfam, pfam: input files are in fasta file format; headers differ between them
        header = ''
        id = ''
        name = ''
        for record in SeqIO.parse(file, "fasta"):
            header = record.description

            if toolType=='rfam' or toolType=='pfam':
                id = header.split('/')[0] # get acession ID
                name = '_'.join(header.split(' ')[1:])[:-1] # get name from header: concatenate to string + remove terminal point of the header + replace possible spaces with underscore; name will remain empty for Pfam file for now
            elif toolType=='literature1':
                id = header.split(':')[0]
                name = '_'.join(header.split(' ')[1:])
            else: #literature2
                id = header.split('|')[0]
                name = header.split('|')[-1].replace(" ", "_")
            #print(f"{id, name} was parsed")
            inputTable[id] = name

    ###################################

    # check validity of --tooltype and extract necessary columns for the given input file

    if toolType=='rfam':
        for id, column in inputTable.items():
            info[id] = column

    elif toolType=='pfam':
        for id, column in inputTable.items():
            info[id] = get_name(id) # no species name available in input file, retrieve it via get_name function

    elif toolType=='cmsearch':
        for id, columns in inputTable.items():
            if columns[15]=='!': # check whether the entry is within inclusion threshold of the results
                info[id] = '_'.join(columns[16:]) # concatenate name columns (were split due to csv space delimiter)
            else:
                continue

    elif toolType=='hmmsearch':
        for id, columns in inputTable.items():
            if columns[16]=='1': # check whether the entry is within inclusion threshold of the results
                info[id] = '_'.join(columns[17:]) # concatenate name columns (were split due to csv space delimiter)
            else:
                continue

    elif toolType=='pdb':
        for id, column in inputTable.items():
            info[id] = column

    elif toolType=='literature1' or toolType=='literature2':
        for id, column in inputTable.items():
            info[id] = column

    else:
        print('Invalid tool type option!')
        exit(1)


    ###################################
    # write output file

    with open(outfile, 'w') as outputStream:
        print("Writing output file.")
        for id, name in info.items():
            try:
                #print(id)
                outputStream.write(f"{id},{name}\n") # output: accession ID + species name per line
            except ValueError:
                continue
    exit(0)
