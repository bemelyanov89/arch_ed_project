python

# entity_extractor.py
import spacy
from typing import List
from .models import Entity, EntityType

class EntityExtractor:
    def __init__(self, model_path: str):
        self.nlp = spacy.load(model_path)
        self.entity_mapping = {
            "ORG": EntityType("DEPARTMENT"),
            "PERSON": EntityType("PERSON"),
            "PRODUCT": EntityType("TECHNOLOGY"),
            "GPE": EntityType("DEPARTMENT")
        }
    
    def extract_entities(self, text: str) -> List[Entity]:
        """Извлекает сущности из текста с использованием NLP"""
        doc = self.nlp(text)
        entities = []
        
        for ent in doc.ents:
            entity_type = self._map_entity_type(ent.label_)
            if entity_type:
                entity = Entity(
                    text=ent.text,
                    type=entity_type,
                    confidence=0.9,  # Базовое значение уверенности
                    context=ent.sent.text if ent.sent else None,
                    start_pos=ent.start_char,
                    end_pos=ent.end_char
                )
                entities.append(entity)
        
        return entities
    
    def _map_entity_type(self, spacy_type: str) -> Optional[EntityType]:
        """Маппит типы сущностей из Spacy в доменные типы"""
        return self.entity_mapping.get(spacy_type)
