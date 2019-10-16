import os
import gzip

from Bio import SeqIO

def batch ( itter , size ):
    entry = True

    while entry:
        data = []
        
        while len ( data ) < size:
            try:
                entry = itter.__next__ ()
            except StopIteration:
                entry = None

            if entry is None:
                break
            
            data.append ( entry )

        if data:
            yield data

handle = gzip.open ( "uniprot.fasta.gz" , "rt" )

for i, data in enumerate ( batch ( SeqIO.parse ( handle , "fasta" ) , 10000 ) ):
    name = "./.uniplot/group-{0}.fasta".format ( i )

    with open ( name , "w" ) as f:
        count = SeqIO.write ( data , f , "fasta" )

    print ( "Wrote {0} records to {1}".format ( count , name ) )