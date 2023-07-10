# TODO: 1. Create a class called Question and QuizBrain. Give the classes the necessary attributes and methods needed.

class Question:
    def __init__(self, question, answer):
        """This Question class takes a text and answer attributes"""
        self.question = question
        self.answer = answer


class QuizBrain:
    def __init__(self, question_list):
        """
         The QuizBrain class takes a list has a tribute
        :param question_list:
        """
        self.question_num = 0
        self.question_list = question_list
        self.score = 0


    # TODO: 4. Check if there is still more question. This is meant as a condition for the While-Loop
    def still_has_question(self) -> object:
        """
        This function checks if there are still questions in the question list
        :rtype: object
        :return: Nothing.
        """
        return self.question_num < len(self.question_list)


    # TODO: 3. display the question to the user to get a reply. The questions must be numbered when displayed
    def next_question(self):
        """
        This function retrieve the question and answer at the corresponding index
        from the 'question_list'. Displays only the question using the input() function
        and asking the user for an answer.
        :param: No parameter
        :return: It returns nothing.
        """
        user_answer = input(f"Q.{self.question_num+1}: {self.question_list[self.question_num].question}."
                            f" (True/False)?: ").title()
        self.is_answer_correct(user_answer)


    # TODO: 4. Check if the user's answer is correct or not and give the user a feedback.
    def is_answer_correct(self, answer):
        """
        This function checks if the user answers is the same with the question answer.
        Gives a report of correct/wrong, with the correct answer and a score
        :param answer:
        :return: Nothing.
        """
        correct_answer = self.question_list[self.question_num].answer
        if correct_answer == answer:
            self.score += 1
            print(f"Correct ✅✅✅!!!!..\nThe correct answer is: {correct_answer}.\n"
                  f"Your score is: ⬆️ {self.score} / {self.question_num + 1}\n")
        else:
            print(f"Wrong ❌❌❌!!!!..\nThe correct answer is: {correct_answer}.\n"
                  f"Your score is: ⬇️ {self.score} / {self.question_num + 1}\n")