import re
import nltk
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("punkt_tab")

class TextPreprocessor:
    def __init__(self):
        self.stop_word = set(stopwords.words("english"))
        self.important_words = {
            "python", "java", "sql", "machine",
            "learning", "deep", "data", "developer",
            "engineering", "experience", "management"
        }
        
        self.stop_word -= self.important_words
    def clean_text(self, text):
        # Remove special characters and digits
        text = re.sub(r"[^a-zA-Z\s]", "", text)
        # Convert to lowercase
        text = text.lower()
        # Tokenize the text
        tokens = nltk.word_tokenize(text)
        # Remove stop words
        tokens = [word for word in tokens if word not in self.stop_word]
        return " ".join(tokens)
    def process_text(self, text):
        cleaned_text = self.clean_text(text)
        return cleaned_text
    
# if __name__ == "__main__":
#     sample_text = """
#     John Doe is a software engineer with experience in Python, Java, and SQL. 
#     He has worked on machine learning and deep learning projects. 
#     His data engineering skills are top-notch.
#     """
#     preprocessor = TextPreprocessor()
#     processed_text = preprocessor.process_text(sample_text)
#     print("Processed Text:")
#     print(processed_text)