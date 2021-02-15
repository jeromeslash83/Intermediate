from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import random


question_bank = []

for dict in question_data:
    question = dict['text']
    answer_to_question = dict['answer']
    question_bank.append(Question(question, answer_to_question))

quiz = QuizBrain(question_bank)
