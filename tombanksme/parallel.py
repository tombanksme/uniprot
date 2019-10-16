import queue

from tombanksme.cache import Cache
from tombanksme.filesystem import Filesystem

from threading import Thread

class Parallel:

    def __init__ ( self ):
        self.cache      =   Cache ()
        self.filesystem =   Filesystem ()

    def worker ( self , q , func ):
        data = []

        while not q.empty ():
            for record in self.filesystem.read ( '.uniplot/' + q.get () ):
                data.append ( func ( record ) )

            q.task_done ()

        return data

    def execute ( self , func , count=5 ):
        q = queue.Queue ()

        # Get the cache groups

        for x in self.cache.get ():
            q.put ( x )

        # Create a pool of threads

        threads = []

        for x in range ( count ):
            t = AdvancedThread ( target=self.worker , args=[ q , func ] )
            t.start ()

            threads.append ( t )

        # Block while we wait for the queue to complete

        q.join ()

        # Clean up the pool of threads

        data = []

        for t in threads:
            _return = t.join ()

            if ( _return is not None ):
                data += _return

        return data

# IDEA: Advanced thread class for getting data from t.join

class AdvancedThread (Thread):

    def __init__ ( self, group=None, target=None, name=None, args=(),
        kwargs={}, Verbose=None ):
        self._return = None
        Thread.__init__ ( self, group, target, name, args, kwargs )

    def run ( self ):
        if self._target is not None:
            self._return = self._target ( *self._args , **self._kwargs )

    def join ( self , *args ):
        Thread.join ( self , *args )

        return self._return