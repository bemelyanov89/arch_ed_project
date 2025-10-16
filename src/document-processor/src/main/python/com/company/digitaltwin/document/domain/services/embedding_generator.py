# embedding_generator.py
from sentence_transformers import SentenceTransformer
import numpy as np
from .models import Embedding

class EmbeddingGenerator:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.dimension = 384  # Для all-MiniLM-L6-v2
    
    def generate_embedding(self, text: str) -> Embedding:
        """Генерирует векторное представление для текста"""
        vector = self.model.encode([text])[0]
        
        return Embedding(
            vector=vector.tolist(),
            model_name=self.model_name,
            dimension=self.dimension
        )
    
    def generate_batch_embeddings(self, texts: List[str]) -> List[Embedding]:
        """Генерирует эмбеддинги для батча текстов"""
        vectors = self.model.encode(texts)
        
        return [
            Embedding(
                vector=vector.tolist(),
                model_name=self.model_name,
                dimension=self.dimension
            )
            for vector in vectors
        ]
