"""back_translator module"""
from .base import LlamaClient
class BackTranslator:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "You augment training data while preserving meaning and labels."
    def augment(self, text: str, label: str = "", method: str = "paraphrase") -> str:
        return self.client.generate(f"Augment this text using {method}:\nText: {text}\nLabel: {label}\n\nGenerate 3 variations that preserve the original meaning/label.", self.system_prompt)
