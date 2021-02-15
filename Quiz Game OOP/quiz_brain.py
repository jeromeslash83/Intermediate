class QuizBrain:

    def __init__(self, all_questions):
        self.question_number = 0
        self.questions_list = all_questions
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}: (True/False)\n").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, answer):
            if user_answer == answer:
                self.score += 1
                print("Correct!")
            else:
                print("Wrong.")
        else:
            pass

        print(f"The correct answer is: {answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.")

        
