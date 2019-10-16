import gzip

from Bio import SeqIO

class Filesystem:

    def gzip ( self , location ):
        return SeqIO.parse (
            gzip.open ( location , "rt" ) , "fasta" )

    def read ( self , location ):
        return SeqIO.parse (
            open ( location ) , "fasta" )
    
    def write ( self , location , data ):
        with open ( location , "w" ) as f:
            SeqIO.write ( data , f , "fasta" )