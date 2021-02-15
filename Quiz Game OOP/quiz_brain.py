class QuizBrain:

    def __init__(self, all_questions):
        self.question_number = 0
        self.questions_list = all_questions

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        current_question = input(f"Q.{self.question_number}: {current_question.text}: (True/False)\n")
        

