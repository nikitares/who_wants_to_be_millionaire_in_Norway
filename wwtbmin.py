import random

#hint use status 
used_fifty_fifty = False
used_audience_help = False
used_phone_friend = False
used_switch_question = False

#function for checking user input 
def user_answer_check(user_answ):
                if user_answ not in ["A", "B", "C", "D", "HINT"]:
                    print("ERORR! Enter a valid letter from A to D\n")
                    return True

#differnt class hints 
class Hint:
    def __init__(self, correct_answer, wrong_answers):
        self.correct_answer = correct_answer
        self.wrong_answers = wrong_answers
        
    def ask_hint(self):
        user_hint = input("\033[35m1) 50/50 2) Ask the audience 3) Phone a friend 4) Switch the question\n Enter a number of hint: ")
        print("")
        if user_hint == "1":
            global used_fifty_fifty
            if used_fifty_fifty == True:
                print("Sorry, you've already used the 50/50 help.")
                return
                
            used_fifty_fifty = True

            if self.fifty_fifty() == True:
                return True 
            else:
                print("\n\033[91mIncorrect!")
                print("You lost :(\033[0m")
                quit()

        elif user_hint == "2":
            global used_audience_help
            if used_audience_help == True:
                print("Sorry, you've already used the audience help.")
                return

            used_audience_help = True
            self.ask_the_audience()
            pass

        elif user_hint == "3":
            global used_phone_friend
            if used_phone_friend == True:
                print("Sorry, you've already used the call a friend help.")
                return

            used_phone_friend = True 
            self.phone_a_friend()
            pass

        elif user_hint == "4":
            global used_switch_question
            if used_switch_question == True:
                print("Sorry, you've already used the switch question help.")
                return
            
            used_switch_question = True 
            if self.switch_the_question() == True:
                return True 
            
    def fifty_fifty(self):
            choices = [self.correct_answer]
            for answer in random.sample(self.wrong_answers, 1):
                choices.append(answer)
            random.shuffle(choices)

            while True:
                for i, answer in enumerate(choices):
                    letter = chr(ord('A') + i) #what is this doing 
                    print(f"{letter}. {answer}")
                user_answer = input("Enter the letter of the correct answer: ").upper()
                print("")

            #function which checks user answer                      
                if user_answer_check(user_answer) == True or user_answer == "HINT":
                    continue
                
                correct_answer_index = ord(user_answer) - ord('A')
                if choices[correct_answer_index] == self.correct_answer: 
                    return True 
                else:
                    return False
                    
    def ask_the_audience(self):
            # Generate a list of probabilities for each answer choice
            total_choices = len(self.wrong_answers) + 1
            remaining_prob = 1.0
            audience_choices = []
            for i in range(total_choices - 1):
                choice_prob = random.triangular(0, remaining_prob)
                remaining_prob -= choice_prob
                audience_choices.append(choice_prob)
            audience_choices.append(remaining_prob)

            audience_votes = {
                self.correct_answer: audience_choices[0]
            }
            for i, answer in enumerate(self.wrong_answers):
                audience_votes[answer] = audience_choices[i+1]
            
            # Print the results
            print("The audience votes are:")
            for answer, prob in audience_votes.items():
                print(f"{answer}: {prob*100:.1f}%")

    def phone_a_friend(self):
        all_answers =  self.wrong_answers + [self.correct_answer]
        answer_probabilities = [0.7 if answer == self.correct_answer else 0.1 for answer in all_answers]
        answer = random.choices(all_answers, weights=answer_probabilities)[0]
        print(f"Your friend thinks the answer is {answer}")

    def switch_the_question(self):
        questions = [
        {"question": "What is the name of the traditional Norwegian dish made of sheep's head, often served during Christmas?",
         "answers": ["Fårikål", "Pinnekjøtt", "Smalahove", "Rakfisk"],
         "correct_answer": "Smalahove"},
        {"question": "What is the name of the Norwegian island that is the northernmost point of the country and also home to a Russian settlement?",
         "answers": ["Svalbard", "Jan Mayen", "Hopen", "Bear Island"],
         "correct_answer": "Svalbard"},
        {"question": "What is the name of the unique Norwegian cheese that is caramelized on the surface and often served as a dessert?",
         "answers": ["Jarlsberg", "Gudbrandsdalsost", "Norvegia", "Brunost"],
         "correct_answer": "Brunost"},
        {"question": "What is the name of the Norwegian town that claims to be the inspiration for the kingdom of Arendelle in Disney's Frozen?",
         "answers": ["Ålesund", "Bergen", "Arendal", "Oslo"],
         "correct_answer": "Arendal"},
        {"question": "What is the name of the longest road tunnel in the world, located in Norway?",
         "answers": ["Lærdal Tunnel", "Eiksund Tunnel", "Toven Tunnel", "Hvalfjörður Tunnel"],
         "correct_answer": "Lærdal Tunnel"}
        ]

        question = random.choice(questions)

        print(question["question"])
        random.shuffle(question["answers"])
        while True:
            answerz = question["answers"]
            for i, answer in enumerate(answerz):
                letter = chr(ord('A') + i) #what is this doing 
                print(f"{letter}. {answer}")
            
            user_answer = input("Enter the letter of the correct answer: ").upper()
            print("")

            if user_answer_check(user_answer) == True:
                continue
            
            correct_answer_index = ord(user_answer) - ord('A')
            if answerz[correct_answer_index] == question["correct_answer"]: 
                return True 
            else:
                print("\n\033[91mIncorrect!")
                print("You lost :(\033[0m")
                quit()
    
class Question:
    def __init__(self, prompt, correct_answer, wrong_answers, reward):
        self.prompt = prompt
        self.correct_answer = correct_answer
        self.answers = [correct_answer] + wrong_answers
        random.shuffle(self.answers)
        self.reward = reward
        #Here I use class Hint 
        self.hint = Hint(correct_answer, wrong_answers)
    
    def ask(self):
        while True:

            print(self.prompt)
            for i, answer in enumerate(self.answers):
                letter = chr(ord('A') + i) #what is this doing 
                print(f"{letter}. {answer}")
            user_answer = input("Enter the letter of the correct answer or HINT: ").upper()
            print("")

            #function which checks user answer                      
            if user_answer_check(user_answer) == True:
                continue

            if user_answer == "HINT":
                if self.hint.ask_hint() == True:
                    print(f"\033[32mCorrect! You have {self.reward} kroner!\033[0m\n")
                    return self.reward
                else:
                    print("\033[0m")
                    continue
            
            else:
                correct_answer_index = ord(user_answer) - ord('A')
                if self.answers[correct_answer_index] == self.correct_answer:
                    print(f"\033[32mCorrect! You have {self.reward} kroner!\033[0m\n")
                    return self.reward
                else:
                    print("\033[91mIncorrect!")
                    print("You lost :(\033[0m")
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
        welcome_message = f"\nWelcome to 'Who Wants to Be a Millionaire in Norway'!Get ready to test your knowledge and win big. You will be presented with 15 questions of increasing difficulty, and for each question you answer correctly, you'll move closer to the grand prize of one million kroner. Let's get started!\n"
        print(welcome_message)
        for question in self.questions:
            question.ask()
        print("You won! Game over. Thanks for playing!")

game = Game(questions)
game.play()