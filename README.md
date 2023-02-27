# who_wants_to_be_millionaire_in_Norway
The game is a console-based quiz game, where the player has to answer multiple-choice questions to progress. The game offers four different types of hints,
namely "50/50", "Ask the audience", "Phone a friend", and "Switch the question". The player can use each hint only once throughout the game.

The "50/50" hint eliminates two of the incorrect answer choices, leaving the player with only two options to choose from.
The "Ask the audience" hint gives the player the probability of each answer choice based on a simulated audience poll.
The "Phone a friend" hint simulates a phone call to a knowledgeable friend who offers their opinion on the correct answer. 
Finally, the "Switch the question" hint offers a new question instead of the current one.

To start the game, the player needs to run the script, and a question is presented with four possible answer choices. 
The player needs to input the letter of the answer they think is correct. If the answer is correct, the player moves on to the next question. 
If the answer is incorrect, the game ends, and the player loses.

During the game, the player can use hints to help them progress through the questions. 
However, the player can use only one hint per question. The player can use the hints by inputting a number that corresponds to the hint they want to use.

The game offers a system of global variables that help keep track of which hints the player has already used. 
If the player tries to use the same hint more than once, the game informs them that they have already used that hint and cannot use it again.

The game also includes a "user_answer_check" function that checks if the player's input is valid. 
If the player enters an invalid input or the hint number, the game prompts the player to enter a valid letter or the correct hint number.

Overall, the game is an entertaining quiz game that offers various hints to help players progress through the questions. 
The game is interactive and engaging and is suitable for players who enjoy quiz games.
