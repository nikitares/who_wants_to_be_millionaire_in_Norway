class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

    def ask(self):
        user_answer = input(self.prompt + '\n')
        return user_answer == self.answer

questions = [
    Question("What is the capital of Norway?", "Oslo"),
    Question("What is the largest city in Norway?", "Oslo"),
    Question("What is the name of the famous Norwegian composer?", "Edvard Grieg"),
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