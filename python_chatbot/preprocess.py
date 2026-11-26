import nltk
from nltk.tokenize import word_tokenize
import re

nltk.download("punkt")
nltk.download("punkt_tab")


def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)

    text = re.sub(r"\s+", " ", text).strip()
    tokens = word_tokenize(text)
    return " ".join(tokens)
question = "What is Python Programming?"

processed = preprocess_text(question)

print("Original:", question)
print("Processed:", processed)