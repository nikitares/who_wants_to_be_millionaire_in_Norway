import random

class Question:
    def __init__(self, prompt, correct_answer, wrong_answers, reward):
        self.prompt = prompt
        self.correct_answer = correct_answer
        self.answers = [correct_answer] + wrong_answers
        random.shuffle(self.answers)
        self.reward = reward
    
    def fifty_fifty(self):
        choices = [self.correct_answer]
        random.shuffle(self.answers)
        for answer in self.answers:
            if answer != self.correct_answer:
                choices.append(answer)
            if len(choices) == 2:
                break
        return choices
    
    #create def answer_check for user_answer 

    def ask(self, fifty_fifty_used = True):
        while True:

            if fifty_fifty_used == False:
                fifty_fifty_message = "\nYou can use 50/50 help(input \"50\")"
            elif fifty_fifty_used == True:
                fifty_fifty_message = ""
            
            print(self.prompt + fifty_fifty_message)
            for i, answer in enumerate(self.answers):
                letter = chr(ord('A') + i) #what is this doing 
                print(f"{letter}. {answer}")
            user_answer = input("Enter the letter of the correct answer: ").upper()
            print("")

            if user_answer not in ["A", "B", "C", "D", "50"]:
                print("ERORR! Enter a valid letter from A to D\n")
                continue  # ask the same question again

            elif user_answer == "50" and fifty_fifty_used == False:
                for i, answer in enumerate(self.fifty_fifty()):
                    letter = chr(ord('A') + i)
                    print(f"{letter}. {answer}")
                user_answer = input("Enter the letter of the correct answer: ").upper()
                print("")
                fifty_fifty_used = True
            
            elif user_answer == "50" and fifty_fifty_used == True:
                print("You used your 50/50 hint\n")
                continue
            
            #here mistake and thats why 50/50 isnt working 
            correct_answer_index = ord(user_answer) - ord('A')
            if self.answers[correct_answer_index] == self.correct_answer:
                print(f"Correct! You have {self.reward} kroner!\n")
                return self.reward
            else:
                print("Incorrect!")
                print("You lost :(")
                quit()

#all questions it takes it from here(maybe letter i want to read this qustions from different file)
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
        #\033[0;32;1m this line of code is responsible for color 
        welcome_message = f"\n\033[0;32;1mWelcome to 'Who Wants to Be a Millionaire in Norway'!Get ready to test your knowledge and win big. You will be presented with 15 questions of increasing difficulty, and for each question you answer correctly, you'll move closer to the grand prize of one million kroner. Let's get started!\n"
        print(welcome_message)
        for question in self.questions:
            question.ask()
        print("Game over. Thanks for playing!")

# Create a new game and play it
game = Game(questions)
game.play()