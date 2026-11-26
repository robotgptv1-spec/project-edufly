import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import preprocess_text


# Load knowledge base
with open("D:/edufly/python_chatbot/knowledge.json", "r") as file:
    knowledge_base = json.load(file)


# Extract questions
questions = [
    item["question"] for item in knowledge_base
]

# Preprocess questions
processed_questions = [
    preprocess_text(q) for q in questions
]


# TF-IDF
vectorizer = TfidfVectorizer()

question_vectors = vectorizer.fit_transform(
    processed_questions
)


def get_answer(user_question):

    processed_input = preprocess_text(user_question)

    input_vector = vectorizer.transform([processed_input])

    similarities = cosine_similarity(
        input_vector,
        question_vectors
    )

    best_match_index = similarities.argmax()

    best_score = similarities[0][best_match_index]

    if best_score < 0.2:
        return "Sorry, I don't know the answer yet."

    return knowledge_base[best_match_index]["answer"]


# Testing
while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = get_answer(user_input)

    print("Chatbot:", response)