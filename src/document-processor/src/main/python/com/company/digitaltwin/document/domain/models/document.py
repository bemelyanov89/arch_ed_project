python

# document.py
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Dict
from enum import Enum

class DocumentSource(Enum):
    CONFLUENCE = "confluence"
    ESED = "esed"
    MANUAL = "manual"

class ProcessingStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass(frozen=True)
class DocumentId:
    value: str
    
    def __post_init__(self):
        if not self.value or len(self.value) < 3:
            raise ValueError("Document ID must be at least 3 characters long")

@dataclass
class Document:
    id: DocumentId
    source: DocumentSource
    original_id: str
    title: str
    content: str
    metadata: Dict[str, str]
    processed_at: Optional[datetime] = None
    status: ProcessingStatus = ProcessingStatus.PENDING
    
    def mark_as_processing(self):
        self.status = ProcessingStatus.PROCESSING
    
    def mark_as_completed(self, processed_at: datetime):
        self.status = ProcessingStatus.COMPLETED
        self.processed_at = processed_at
    
    def mark_as_failed(self):
        self.status = ProcessingStatus.FAILED
    
    def is_processable(self) -> bool:
        return (self.status == ProcessingStatus.PENDING and 
                self.content and len(self.content.strip()) > 0)
