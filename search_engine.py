import faiss
import numpy as np

class PaperSearchEngine:
    def __init__(self, embeddings, papers):
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)
        self.papers = papers

    def search(self, query_embedding, top_k=5):
        distances, indices = self.index.search(query_embedding, top_k)
        return [self.papers[i] for i in indices[0]]
