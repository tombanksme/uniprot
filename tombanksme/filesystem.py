import gzip

from Bio import SeqIO

class Filesystem:

    def gzip ( self , location ):
        return SeqIO.parse (
            gzip.open ( location , "rt" ) , "uniprot-xml" )