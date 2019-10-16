import os

from tombanksme.filesystem import Filesystem

class Cache:

    def __init__ ( self ):
        self.filesystem = Filesystem ()

    def get ( self ):
        return os.listdir ( '.uniplot' )

    def build ( self , location ):
        records = self.filesystem.gzip ( location )

        os.mkdir ( '.uniplot' )

        for x , data in enumerate ( self.batch ( records , 10000 ) ):
            self.filesystem.write (
                ".uniplot/group-{0}.fasta".format ( x ) , data )
    
    def batch ( self , itter , size ):
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

    def exists ( self ):
        return os.path.isdir ( '.uniplot' )