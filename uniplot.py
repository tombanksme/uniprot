import math

from functools import reduce

from tombanksme.cache import Cache
from tombanksme.parallel import Parallel

location = "uniprot.fasta.gz"

def length ( parallel ):
    return len (
        parallel.execute ( lambda a : 1 ) )

def average_length ( parallel ):
    data = parallel.execute (
        lambda a : len ( a.seq ) )

    return math.floor (
        reduce (
            lambda a,b: a+b , data ) / len ( data ) )
    
# If no cache exists build one

cache = Cache ()

if not cache.exists ():
    print ( "Building cache for: {0}".format ( location ) )
    cache.build ( location )

# Execute the average length query

parallel = Parallel ()

print ( length ( parallel ) )