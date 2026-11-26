import re

class SkillExtractor:
    def __init__(self):
        self.skills = {

            "Programming Languages": [
                "python",
                "java",
                "javascript",
                "c",
                "c++",
                "c#",
                "php",
                "ruby",
                "go"
            ],

            "Web Development": [
                "html",
                "css",
                "react",
                "angular",
                "node.js",
                "express",
                "flask",
                "django"
            ],

            "Database": [
                "sql",
                "mysql",
                "postgresql",
                "mongodb",
                "firebase",
                "oracle"
            ],

            "Machine Learning & AI": [
                "machine learning",
                "deep learning",
                "tensorflow",
                "pytorch",
                "scikit-learn",
                "pandas",
                "numpy",
                "opencv",
                "nlp"
            ],

            "Tools": [
                "git",
                "github",
                "docker",
                "aws",
                "linux",
                "vscode"
            ]

        }
        
    def extract_skills(self,text):
        text = text.lower()
        extracted_skills = {}

        for category, skills in self.skills.items():
            found_skills = [skill for skill in skills if re.search(r'\b' + re.escape(skill) + r'\b', text)]
            if found_skills:
                extracted_skills[category] = found_skills

        return extracted_skills
    
    def get_all_skills(self):
        all_skills = []
        for skills in self.skills.values():
            all_skills.extend(skills)
        return all_skills
    
# if __name__ == "__main__":
#     sample_text = """
#     John Doe is a software engineer with experience in Python, Java, and SQL. 
#     He has worked on machine learning and deep learning projects. 
#     His data engineering skills are top-notch.
#     """
#     skill_extractor = SkillExtractor()
#     extracted_skills = skill_extractor.extract_skills(sample_text)
#     print("Extracted Skills:")
#     print(extracted_skills)