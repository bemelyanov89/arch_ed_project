# document_classifier.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
from typing import List

class DocumentClassifier:
    def __init__(self, model_path: Optional[str] = None):
        self.vectorizer = TfidfVectorizer(max_features=1000)
        self.model = LogisticRegression()
        self.classes = ["TECHNICAL", "BUSINESS", "PROCESS", "OTHER"]
        
        if model_path:
            self.load_model(model_path)
    
    def classify_document(self, text: str) -> str:
        """Классифицирует тип документа"""
        features = self.vectorizer.transform([text])
        prediction = self.model.predict(features)[0]
        return self.classes[prediction]
    
    def train(self, texts: List[str], labels: List[str]):
        """Обучает модель классификации"""
        features = self.vectorizer.fit_transform(texts)
        self.model.fit(features, labels)
    
    def save_model(self, path: str):
        """Сохраняет модель"""
        joblib.dump({
            'vectorizer': self.vectorizer,
            'model': self.model
        }, path)
    
    def load_model(self, path: str):
        """Загружает модель"""
        data = joblib.load(path)
        self.vectorizer = data['vectorizer']
        self.model = data['model']
