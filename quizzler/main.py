from quizzler_brain import QuizBrain, Question
from data import question_data, logo

# TODO: 2. Create a list of question and call it 'question_bank'.
# Declaring the question_bank 👇🏾 and appending it elements later
question_bank = []
for item in question_data:
    question = item["text"]
    answer = item["answer"]
    question_bank.append(Question(question, answer))

print(logo)
quizzler = QuizBrain(question_bank)

while quizzler.still_has_question():
    quizzler.next_question()
    quizzler.question_num += 1