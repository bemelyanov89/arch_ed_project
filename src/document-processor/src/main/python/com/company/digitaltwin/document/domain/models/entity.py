python

# entity.py
@dataclass(frozen=True)
class EntityType:
    value: str
    
    VALID_TYPES = {"TECHNOLOGY", "BUSINESS_PROCESS", "SYSTEM", "PERSON", "DEPARTMENT"}

    def __post_init__(self):
        if self.value not in self.VALID_TYPES:
            raise ValueError(f"Invalid entity type: {self.value}")

@dataclass
class Entity:
    text: str
    type: EntityType
    confidence: float
    context: Optional[str] = None
    start_pos: Optional[int] = None
    end_pos: Optional[int] = None
    
    def is_high_confidence(self) -> bool:
        return self.confidence >= 0.8
