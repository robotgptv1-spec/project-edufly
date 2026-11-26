from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

class MatchingEngine:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english',ngram_range=(1, 2))
        
    def calculate_similarity(self, resume_text, job_description):
        # Combine the resume text and job description into a list
        documents = [resume_text, job_description]
        
        # Transform the documents into TF-IDF vectors
        tfidf_matrix = self.vectorizer.fit_transform(documents)
        
        # Calculate cosine similarity between the resume and job description
        similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        
        return similarity_score[0][0]

# if __name__ == "__main__":
#     resume_text = """
#     John Doe is a software engineer with experience in Python, Java, and SQL. 
#     He has worked on machine learning and deep learning projects. 
#     His data engineering skills are top-notch.
#     """
    
#     job_description = """
#     We are looking for a software engineer with strong skills in Python, Java, and SQL. 
#     Experience in machine learning and deep learning is a plus. 
#     Data engineering experience is highly desirable.
#     """
    
#     matching_engine = MatchingEngine()
#     similarity_score = matching_engine.calculate_similarity(resume_text, job_description)
    
#     print(f"Similarity Score: {similarity_score:.4f}")