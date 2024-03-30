import pandas as pd

# Load the dataset
data = pd.read_csv("data.csv")


# Function to quiz user
def quiz(data):
    score = 0
    for index, row in data.iterrows():
        print("Question:", row["Question"])
        user_response = input("Your answer: ")
        if user_response == row["Réponse correcte"]:
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
