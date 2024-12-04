#response_generator.py
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModelForSequenceClassification
import torch

class GetResponse:
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        
        # Move to GPU if available
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
    
    def analyze_review(self, review):
        # Tokenize input
        inputs = self.tokenizer(review, return_tensors="pt", truncation=True, max_length=512).to(self.device)
        
        # Perform inference
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        # Get predicted class
        predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
        predicted_class = torch.argmax(predictions, dim=1)
        
        # Convert to sentiment
        sentiment_map = {0: 'negative', 1: 'positive'}
        return sentiment_map.get(predicted_class.item(), 'neutral')