class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.quiz_score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        u_ans = input(f"Q.{self.question_number}: {current_question.text} (True/False) ")
        self.check_answer(u_ans, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.quiz_score += 1
            print("You're right!")
        else:
            print("That's wrong")
        print(f"The correct answer was {correct_answer}. ")
        print(f"You're current score is: {self.quiz_score}/{self.question_number}.")
        print("\n")

