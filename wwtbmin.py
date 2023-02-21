import random

#function for checking user input 
def user_answer_check(user_answ):
                if user_answ not in ["A", "B", "C", "D", "HINT"]:
                    print("ERORR! Enter a valid letter from A to D\n")
                    return True
#create differnt class hints 
class Hint:
    def __init__(self, correct_answer, wrong_answers):
        self.correct_answer = correct_answer
        self.wrong_answers = wrong_answers  
        self.used_audience_help = False
        self.used_phone_friend = False
        self.used_fifty_fifty = False
        self.used_switch_question = False

    def ask_hint(self):
        user_hint = input("1) 50/50 2) Ask the audience 3) Phone a friend 4) Switch the question\n Enter a number of hint: ")
        print("")
        if user_hint == "1":
            if self.used_fifty_fifty == True:
                print("Sorry, you've already used the 50/50 help.")
                quit()

            
            self.used_fifty_fifty = True

            while True:
                choice = self.fifty_fifty()
                for i, answer in enumerate(choice):
                    letter = chr(ord('A') + i) #what is this doing 
                    print(f"{letter}. {answer}")
                user_answer = input("Enter the letter of the correct answer: ").upper()
                print("")

            #function which checks user answer                      
                if user_answer_check(user_answer) == True:
                    continue
                
                
                correct_answer_index = ord(user_answer) - ord('A')
                if choice[correct_answer_index] == self.correct_answer: 
                    return 
                else:
                    quit()

                
        elif user_hint == "2":
        # code to implement "Ask the audience" hint
            pass
        elif user_hint == "3":
        # code to implement "Phone a friend" hint
            pass
        elif user_hint == "4":
        # code to implement "Switch the question" hint
            pass
        else:
            print("Invalid hint choice. Please enter a number between 1 and 4.")  # handle invalid input
            

    def fifty_fifty(self):
            choices = [self.correct_answer]
            for answer in random.sample(self.wrong_answers, 1):
                choices.append(answer)
            random.shuffle(choices)
            return choices


#    def ask_the_audience(self, correct_answer):
#        if not self.used_audience_help:
#            # implementation of the ask_the_audience method
#            self.used_audience_help = True
#        else:
#            print("Sorry, you've already used the ask the audience help.")

#    def phone_a_friend(self, correct_answer):
#        if not self.used_phone_friend:
#            # implementation of the phone_a_friend method
#            self.used_phone_friend = True
#        else:
#            print("Sorry, you've already used the phone a friend help.")



#    def switch_the_question(self):
#        if not self.used_switch_question:
#            # implementation of the switch_the_question method
#            self.used_switch_question = True
#        else:
#            print("Sorry, you've already used the switch the question help.")

class Question:
    def __init__(self, prompt, correct_answer, wrong_answers, reward):
        self.prompt = prompt
        self.correct_answer = correct_answer
        self.answers = [correct_answer] + wrong_answers
        random.shuffle(self.answers)
        self.reward = reward
        #Here I use class Hint 
        self.hint = Hint(correct_answer, wrong_answers)
    
    #create def answer_check for user_answer 

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
                self.hint.ask_hint()
                print(f"Correct! You have {self.reward} kroner!\n")
                return self.reward
            
            else:
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