import logging
import faiss
import numpy as np
import pandas as pd

class Indexing:
    def __init__(self, features, df):
        self.logger = logging.getLogger(__name__)

        self.features = features
        self.index = None
        self.df = df.reset_index(drop=True)
        self.nlist = 100
    
    def create_index(self):

        vectors = np.ascontiguousarray(self.df[self.features].values.astype('float32'))
        
        faiss.normalize_L2(vectors)

        dimension = vectors.shape[1]

        quantizer = faiss.IndexFlatIP(dimension)
        self.index = faiss.IndexIVFFlat(quantizer, dimension, self.nlist)

        self.index.train(vectors)

        self.index.add(vectors)

        self.logger.info(f"Indexing completed. Number of vectors indexed: {self.index.ntotal}")
        return self.index

    def search(self, search, k=10):
        
        search = search.astype('float32')
        faiss.normalize_L2(search)

        distances, indices = self.index.search(search, k)
        return distances, indices
    
    def save_index(self, path):
        faiss.write_index(self.index, path)
        self.logger.info(f"Index saved to {path}")


        