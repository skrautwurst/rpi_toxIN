#!/usr/bin/env python3

"""

Retrieve taxonomy ID for species via accession ID. Output is in csv format containing the taxonomy ID, entry ID, and organism name for each entry in the input file.

Usage:
    retrieve_genus.py [options] <IDFILE> <OUTPUTFILE>

Options:
    -h, --help                                  Show this help message and exit.
    -t IDTYPE, --idtype IDTYPE                  Type/source of accession IDs in the input IDFILE. 1: NCBI nucleotide, 2: NCBI protein, 3: UniProt, 4: PDB, 5: ENA. [default: 1]

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
from docopt import docopt

###################################

Entrez.email = "sarah.krautwurst@uni-jena.de"

def get_taxid_ncbi(dbid, dbtype):  # get taxonomy ID of an NCBI entry
    """
    Gets the species' taxonomy ID of a NCBI entry.

    Parameters:
    dbid -- database ID / entry ID whose taxonomy ID is wanted
    dbtype -- which database to use, based on the entry ID type (nucleotides, proteins) - refers to the script option --idtype

    Return:
    Taxonomy ID for the given NCBI ID/entry.

    """

    while 1:
        try:
            handle = Entrez.elink(dbfrom=dbtype, db='taxonomy', id=dbid, idtype='acc', rettype='xml')
            record = Entrez.read(handle)
            handle.close()
            return record[0]["LinkSetDb"][0]["Link"][0]["Id"]

        except RuntimeError:
            time.sleep(5)
            continue
        except IndexError:
            print(f"Error: No taxonomy ID for entry {dbid}")
            pass
        break


def get_taxid_unipr(dbid):  # get taxonomy ID of an UniProt entry; for Pfam data
    """
    Gets the species' taxonomy ID of an UniProt entry.

    Parameters:
    dbid -- database ID / entry ID whose taxonomy ID is wanted

    Return:
    Taxonomy ID and organism name for the given UniProt ID/entry.

    """

    while 1:
        try:
            handle = ExPASy.get_sprot_raw(dbid)
            record = SwissProt.read(handle)
            handle.close()
            org_name = record.organism[:-1].replace(" ", "_") # remove terminal point and replace spaces
            return [record.taxonomy_id[0], org_name]

        except RuntimeError:
            time.sleep(5)
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

    file = args['<IDFILE>']
    outfile = args['<OUTPUTFILE>']
    idType = int(args['--idtype'])

    ###################################
    # variable declaration

    specIds = {} # dictionary for input file
    taxDict = {} # dictionary will contain the accession ID as key, taxID and organism name as value; content will be written to output file

    ###################################
    # get accession IDs from input IDFILE
    # input file = output from script extract_id-species.py, in csv format, accession IDs in first column (row[0]), organism name in second column (row[1])

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row:
                specIds[row[0]] = (row[1]) # ID and name pairs

    ###################################

    # check validity of --idtype and extract taxIDs for the given input list

    if idType==1: # for cmsearch, rfam, and literature1
        for id, name in specIds.items():
            #taxDict = { id : get_taxid(id, dbname)}
            taxDict[id] = [get_taxid_ncbi(id, 'nuccore'), name]

    elif idType==2: # for hmmsearch and literature2
        for id, name in specIds.items():
            taxDict[id] = [get_taxid_ncbi(id, 'protein'), name]

    elif idType==3: # for pfam
        for id, name in specIds.items():
            taxDict[id] = get_taxid_unipr(id)

    elif idType==4: # for pdb: taxID is already included in the name description, therefore only string editing is necessary to get the wanted information
        for id, name in specIds.items():
            organism = '_'.join(name.split('_')[:-1]).capitalize()
            str = name.split('_')[-1]
            taxDict[id] = [str[str.find("(")+1 : str.find(")")], organism]

    else:
        print('Invalid ID type option!')
        exit(1)

    ###################################
    # write output file
    # taxID in first column for easier filtering later on in the workflow
    with open(outfile, 'w') as outputStream:
        for id, name in specIds.items():
            try:
                if taxDict[id][0] == None:
                    continue
                else:
                    outputStream.write(f"{taxDict[id][0]},{id},{taxDict[id][1]}\n") # output: taxID + accession ID and species name per line
            except ValueError:
                continue
    exit(0)
