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
            letter = chr(ord('A') + i)  # convert index to letter(i need better exp for CHR and ORD)
            print(f"{letter}. {answer}")
        user_answer = input("Enter the letter of the correct answer: ").upper()
        correct_answer_index = ord(user_answer) - ord('A')
        return self.answers[correct_answer_index] == self.correct_answer

questions = [
    Question("What is the capital of Norway?", "Oslo", ["Bergen", "Trondheim", "Stavanger"]),
    Question("What is the largest city in Norway?", "Oslo", ["Bergen", "Trondheim", "Stavanger"]),
    Question("What is the name of the famous Norwegian composer?", "Edvard Grieg", ["Johan Svendsen", "Rikard Nordraak", "Geirr Tveitt"]),
    Question("What is the name of the deepest lake in Norway?", "Hornindalsvatnet", ["Mjøsa", "Lake Tinnsjø", "Randsfjorden"]),
    Question("Which famous Norwegian explorer was the first person to reach the South Pole?", "Roald Amundsen", ["Fridtjof Nansen", "Thor Heyerdahl", "Helge Ingstad"]),
    Question("What is the name of the traditional Norwegian dress, usually worn for special occasions?", "Bunad", ["Lusekofte", "Gákti", "Kofte"]),
    Question("Which Norwegian city is famous for its annual jazz festival?", "Molde", ["Oslo", "Bergen", "Trondheim"]),
    Question("Which Norwegian artist is famous for his painting \"The Scream\"?", "Edvard Munch", ["Gustav Vigeland", "Thorvald Erichsen", "Harald Sohlberg"]),
    Question("In what city is the Holmenkollen ski jump located?", "Oslo", ["Bergen", "Trondheim", "Stavanger"]),
    Question("Which of these is not a Norwegian fjord?", "Vistafjord", ["Geirangerfjord", "Hardangerfjord", "Sognefjord"]),
    Question("What is the currency of Norway?", "Krone", ["Euro", "Pound", "Dollar"]),
    Question("Which of these famous Norwegian playwrights is known for writing 'A Doll\'s House'?", "Henrik Ibsen", ["August Strindberg", "Anton Chekhov", "Samuel Beckett"]),
    Question("Which of these foods is a traditional Norwegian dish?", "Lutefisk", ["Tacos", "Sushi", "Kebab"]),
    Question("What is the highest mountain in Norway?", "Galdhøpiggen", ["Glittertind", "Snøhetta", "Jotunheimen"]),
    Question("Which of these is a traditional Norwegian musical instrument?", "Hardanger fiddle", ["Bagpipes", "Harmonica", "Ukulele"])
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
            print(f"Your score: {self.score} / {len(self.questions)}\n")
        print("Game over. Thanks for playing!")

# Create a new game and play it
game = Game(questions)
game.play()