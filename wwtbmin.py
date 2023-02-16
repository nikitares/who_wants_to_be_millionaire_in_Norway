import random

class Question:
    def __init__(self, prompt, correct_answer, wrong_answers, reward):
        self.prompt = prompt
        self.correct_answer = correct_answer
        self.answers = [correct_answer] + wrong_answers
        random.shuffle(self.answers)
        self.reward = reward

    def ask(self):
        while True:
            print(self.prompt)
            for i, answer in enumerate(self.answers):
                letter = chr(ord('A') + i)
                print(f"{letter}. {answer}")
            user_answer = input("Enter the letter of the correct answer: ").upper()
            if user_answer not in ["A", "B", "C", "D"]:
                print("ERORR! Enter a valid letter from A to D\n")
                continue  # ask the same question again
            else:
                correct_answer_index = ord(user_answer) - ord('A')
                if self.answers[correct_answer_index] == self.correct_answer:
                    print(f"Correct! You have {self.reward} kroner!\n")
                    return self.reward
                else:
                    print("Incorrect!")
                    print("You lost :(")
                    quit()

questions = [
    Question("What is the capital of Norway?", "Oslo", ["Bergen", "Trondheim", "Stavanger"], 25),
    Question("What is the largest city in Norway?", "Oslo", ["Bergen", "Trondheim", "Stavanger"], 50),
    Question("What is the name of the famous Norwegian composer?", "Edvard Grieg", ["Johan Svendsen", "Rikard Nordraak", "Geirr Tveitt"], 100),
    Question("What is the name of the deepest lake in Norway?", "Hornindalsvatnet", ["Mjøsa", "Lake Tinnsjø", "Randsfjorden"], 250),
    Question("Which famous Norwegian explorer was the first person to reach the South Pole?", "Roald Amundsen", ["Fridtjof Nansen", "Thor Heyerdahl", "Helge Ingstad"], 500),
    Question("What is the name of the traditional Norwegian dress, usually worn for special occasions?", "Bunad", ["Lusekofte", "Gákti", "Kofte"], 1000),
    Question("Which Norwegian city is famous for its annual jazz festival?", "Molde", ["Oslo", "Bergen", "Trondheim"], 2500),
    Question("Which Norwegian artist is famous for his painting \"The Scream\"?", "Edvard Munch", ["Gustav Vigeland", "Thorvald Erichsen", "Harald Sohlberg"], 5000),
    Question("In what city is the Holmenkollen ski jump located?", "Oslo", ["Bergen", "Trondheim", "Stavanger"], 10000),
    Question("Which of these is not a Norwegian fjord?", "Vistafjord", ["Geirangerfjord", "Hardangerfjord", "Sognefjord"], 25000),
    Question("What is the currency of Norway?", "Krone", ["Euro", "Pound", "Dollar"], 50000),
    Question("Which of these famous Norwegian playwrights is known for writing 'A Doll\'s House'?", "Henrik Ibsen", ["August Strindberg", "Anton Chekhov", "Samuel Beckett"], 100000),
    Question("Which of these foods is a traditional Norwegian dish?", "Lutefisk", ["Tacos", "Sushi", "Kebab"], 250000),
    Question("What is the highest mountain in Norway?", "Galdhøpiggen", ["Glittertind", "Snøhetta", "Jotunheimen"], 500000),
    Question("Which of these is a traditional Norwegian musical instrument?", "Hardanger fiddle", ["Bagpipes", "Harmonica", "Ukulele"], 1000000)
]

class Game:
    def __init__(self, questions):
        self.questions = questions

    def play(self):
        for question in self.questions:
            question.ask()
        print("Game over. Thanks for playing!")

# Create a new game and play it
game = Game(questions)
game.play()