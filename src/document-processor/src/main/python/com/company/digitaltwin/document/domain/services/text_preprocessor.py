# text_preprocessor.py
import re
import html
from typing import List

class TextPreprocessor:
    def __init__(self):
        self.html_tags = re.compile(r'<[^>]+>')
        self.special_chars = re.compile(r'[^\w\s\.\,\-\–]')
    
    def preprocess_text(self, text: str) -> str:
        """Очищает и нормализует текст"""
        if not text:
            return ""
        
        # Удаление HTML тегов
        cleaned = self.html_tags.sub(' ', text)
        
        # Декодирование HTML entities
        cleaned = html.unescape(cleaned)
        
        # Удаление специальных символов
        cleaned = self.special_chars.sub(' ', cleaned)
        
        # Нормализация пробелов
        cleaned = ' '.join(cleaned.split())
        
        return cleaned.strip()
    
    def extract_sentences(self, text: str) -> List[str]:
        """Разбивает текст на предложения"""
        sentences = re.split(r'[.!?]+', text)
        return [s.strip() for s in sentences if s.strip()]
