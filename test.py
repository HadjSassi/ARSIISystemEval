import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# Load the dataset
data = pd.read_csv("data.csv")


# Function to compute similarity between two texts
def compute_similarity(text1, text2):
    if not text1.strip() or not text2.strip() or text1.lower() in ENGLISH_STOP_WORDS or text2.lower() in ENGLISH_STOP_WORDS:
        return 0  # Return 0 similarity for empty or stop words only texts
    try:
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([str(text1), str(text2)])  # Convert to string
        similarity = cosine_similarity(vectors[0], vectors[1])
        return similarity[0][0]
    except ValueError:
        return 0  # Return 0 similarity if TfidfVectorizer encounters an issue


# Function to quiz user
def quiz(data):
    score = 0
    for index, row in data.iterrows():
        print("Question:", row["Question"])
        user_response = input("Your answer: ")
        similarity_score = compute_similarity(user_response, row["Réponse correcte"])
        print("Similarity score:", similarity_score)  # Print similarity score for debugging
        if similarity_score > 0.4:  # Adjusted threshold
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        print()  # Empty line for readability

        if index == 4:  # Break after 5 questions
            break

    return score


# Run the quiz
total_questions = 5
total_score = quiz(data)

print("Quiz complete!")
print("Total score:", total_score, "/", total_questions)
