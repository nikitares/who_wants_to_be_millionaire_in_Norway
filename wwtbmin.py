import random

class Question:
    def __init__(self, prompt, correct_answer, wrong_answers):
        self.prompt = prompt
        self.correct_answer = correct_answer
        self.answers = [correct_answer] + wrong_answers
        random.shuffle(self.answers)

    def ask(self):
        print(self.prompt)
        for i, answer in enumerate(self.answers):
            print(f"{i+1}. {answer}")
        user_answer = input("Enter the number of the correct answer: ")
        return self.answers[int(user_answer)-1] == self.correct_answer

questions = [
    Question("What is the capital of Norway?", "Oslo", ["Bergen", "Trondheim", "Stavanger"]),
    Question("What is the largest city in Norway?", "Oslo", ["Bergen", "Trondheim", "Stavanger"]),
    Question("What is the name of the famous Norwegian composer?", "Edvard Grieg", ["Johan Svendsen", "Rikard Nordraak", "Geirr Tveitt"]),
    # Add more questions here...
]

class Game:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def play(self):
        for q in self.questions:
            if q.ask():
                self.score += 1
                print("Correct!")
            else:
                print("Incorrect!")
            print(f"Your score: {self.score} / {len(self.questions)}")
        print("Game over. Thanks for playing!")

# Create a new game and play it
game = Game(questions)
game.play()