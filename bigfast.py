import queue
import threading
import os

from Bio import SeqIO

def worker ( q , func ):
    data = []

    while not q.empty ():
        handle = open ( '.uniplot/{0}'.format ( q.get () ) )

        print ( "Acquired new file!" )

        for record in SeqIO.parse ( handle , "fasta" ):
            data.append ( func ( record ) )

        q.task_done ()
    
    print ( data )

q = queue.Queue ()

for x in os.listdir ( ".uniplot" ):
    q.put ( x )

threads = []

for x in range ( 5 ):
    t = threading.Thread ( target=worker , args=[ q , lambda a : len ( a.seq ) ] )
    t.start ()

    threads.append ( t )

q.join ()

for t in threads:
    t.join ()