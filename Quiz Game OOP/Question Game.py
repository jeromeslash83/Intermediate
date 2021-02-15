from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for dict in question_data:
    question = dict['text']
    answer_to_question = dict['answer']
    question_bank.append(Question(question, answer_to_question))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    
print("\n\nYou've completed the quiz!")
print(f"Your final score is {quiz.score} / {quiz.question_number}.")
        
