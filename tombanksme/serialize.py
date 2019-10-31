import gzip
import pickle

class Serialize:

    def load ( self , location ):
        with gzip.open ( location , "rb" ) as f:
            return pickle.load ( f )

    def dump ( self , obj , location ):
        with gzip.open ( location , "wb" ) as f:
            pickle.dump ( obj , f )