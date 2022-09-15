from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create an empty list to store the questions
question_bank = []

# Loop through the question_data list and create a new Question object for each question
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

# Create a new QuizBrain object and pass in the question_bank list
quiz = QuizBrain(question_bank)

# Loop through the question_bank list and ask the user each question
while quiz.still_has_questions():
    quiz_object = quiz.next_question()

print("You've completed the quiz")
print(f"your finale score was: {quiz.score}/{quiz.question_number}")