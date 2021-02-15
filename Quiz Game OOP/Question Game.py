from data import question_data
from question_model import Question
import random


question_bank = []

for dict in question_data:
    question = dict['text']
    answer_to_question = dict['answer']
    question_bank.append(Question(question, answer_to_question))
