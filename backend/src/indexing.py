import logging
import faiss
import numpy as np
import pandas as pd

class Indexing:
    def __init__(self, features):
        self.logger = logging.getLogger(__name__)

        self.features = features
        self.index = None
        self.nlist = 100
    
    def index(self, df):

        vectors = df[self.features].values.astype('float32')
        faiss.normalize_L2(vectors)

        dimension = vectors.shape[1]

        quantizer = faiss.IndexFlatIP(dimension)
        self.index = faiss.IndexIVFFlat(quantizer, dimension, self.nlist, faiss.METRIC_INNER_PRODUCT)

        self.index.train(vectors, niter=20)

        self.index.add(vectors)

        self.logger.info(f"Indexing completed. Number of vectors indexed: {self.index.ntotal}")
        return self.index

    def search(self, search, k=10):
        
        search = search.astype('float32')
        faiss.normalize_L2(search)

        distances, indices = self.index.search(search, k)
        return distances, indices
    

        