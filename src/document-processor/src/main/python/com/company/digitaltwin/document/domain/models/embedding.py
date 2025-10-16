python 

# embedding.py
@dataclass
class Embedding:
    vector: List[float]
    model_name: str
    dimension: int
    
    def __post_init__(self):
        if len(self.vector) != self.dimension:
            raise ValueError(f"Vector dimension mismatch: expected {self.dimension}, got {len(self.vector)}")

@dataclass
class ProcessingResult:
    document_id: DocumentId
    entities: List[Entity]
    embedding: Embedding
    processing_time: float
    metadata: Dict[str, any]
