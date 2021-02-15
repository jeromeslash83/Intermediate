from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import random

question_bank = []

for dict in question_data:
    question = dict['question']
    answer_to_question = dict['correct_answer']
    question_bank.append(Question(question, answer_to_question))

questions = random.sample(question_bank, 12)
quiz = QuizBrain(questions)

while quiz.still_has_questions():
    quiz.next_question()
    
print("\n\nYou've completed the quiz!")
print(f"Your final score is {quiz.score} / {quiz.question_number}.")
        
