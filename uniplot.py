import math

from functools import reduce

from tombanksme.cache import Cache
from tombanksme.parallel import Parallel

location = "uniprot.small.xml.gz"

def count ( parallel ):
    data = parallel.execute ( lambda a : 1 )

    return len ( data )

# Thread Count: 17s

def average_length ( parallel ):
    data = parallel.execute (
        lambda a : len ( a.seq ) , count=5 )

    return reduce (
        lambda a,b: a+b , data ) / len ( data )
    
# If no cache exists build one

cache = Cache ()

if not cache.exists ():
    print ( "Building cache for: {0}".format ( location ) )

    cache.build ( location )

    print ( "Successfully generated cache" )

# Begin parallel threads and count

parallel = Parallel ()

print ( average_length ( parallel ) )