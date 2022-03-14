"""A collection of functions for doing my project.

All functions are original except scramble_names().
"""

import random
from random import shuffle
from random import sample

score = 0

character_list = ['IRON MAN', 'CAPTAIN AMERICA', 'HULK', 'BLACK WIDOW', 'HAWKEYE', 'THOR']


def pick_character(character_list):
    """Picks a character from character_list.
    
    Parameters
    ----------
    character_list : list
        A list of Marvel characters.
    
    Returns
    -------
    random.sample(character_list, 1)[0] : str
        A randomly sampled character from character_list.
    """
    
    # indexes into 0th position to get the string rather than a list
    return random.sample(character_list, 1)[0]


def scramble_names(character_name):
    """Shuffles the order of letters in the character_name string.
    
    Parameters
    ----------
    character_name : str
        Uses the pick_character() function to randomly select a character from character_list.
        character_name = pick_character(character_list)
    
    Returns
    -------
    ''.join(name) : str
        A shuffled/scrambled version of character_name.
        
    Uses external code.
    Citation: https://stackoverflow.com/questions/6181304/are-there-any-ways-to-scramble-strings-in-python
    """
    
    # converts the name to a list, shuffles the letters, rejoins them into a string
    name = list(character_name)
    shuffle(name)
    return ''.join(name)


def change_case(user_input):
    """Changes the user's input to be uppercase.
    Items in character_list are uppercase.
        Allows compare_response() to work when matching user input to the corresponding character in character_list.
    
    Parameters
    ----------
    user_input : str
        What the user types in for user_input in the play_game() function.
        user_input = input('Input your response: ')
    
    Returns
    -------
    user_input : str
        Updated version of user_input as uppercase.
    """
    
    user_input = user_input.upper()
    return user_input


def compare_response(character_name, response):
    """Checks if the user's response matches character_name.
    The output reply changes depending on the user's response.
    User can input 'GIVE UP' to see the answer, and 'QUIT' to quit the game.
    
    Parameter
    ---------
    character_name : str
        Uses the pick_character() function to randomly select a character from character_list.
        character_name = pick_character(character_list)  
    response : str
        What the user inputs for the 'response' variable in the play_game() function.
        response = change_case(user_input)
            user_input = input('Input your response: ')
    
    Returns
    -------
    reply : str
        Tells user if the response is correct or incorrect.
        If user wants to give up, tells user the correct answer.
        If user wants to quit, responds with 'Bye!'
    """
    
    if response == character_name:
        reply = 'Correct!'
    elif response == 'GIVE UP':
        reply = 'The answer is ' + character_name
    elif response == 'QUIT':
        reply = 'Goodbye!'
    else:
        reply = 'Incorrect. The answer is ' + character_name
    
    return reply


def add_score(character_name, response):
    """Computes player's score using the score variable defined at the top.
    Uses compare_response() function to check if user's response was correct or not.
    Increases score by 1 when player is correct. Does not add to score otherwise.
    
    Parameters
    ----------
    character_name : str
        Uses the pick_character() function to randomly select a character from character_list.
        character_name = pick_character(character_list)
    response : str
        What the user inputs for the 'response' variable in the play_game() function.
        response = change_case(user_input)
            user_input = input('Input your response: ')
    
    Returns
    -------
    score : int
        Updated score after each response from the user.
    """
    
    global score
    
    if compare_response(character_name, response) == 'Correct!':
        score += 1
    else:
        score += 0
    
    return score


def play_game(character_list):
    """Executes the game once through.
    
    Parameters
    ----------
    character_list : list
        A list of Marvel characters.    
    
    Returns
    -------
    output : tuple
        Includes 3 parts:
            - User's response.
            - Reply from the compare_response() function.
            - Score from the add_score() function.
    """
    
    # part 1: chooses character from list, scrambles the name, displays scrambled name for user
    character_name = pick_character(character_list)
    shuffled_name = scramble_names(character_name)
    print(shuffled_name)

    # part 2: compares user input to the actual name and computes user's score
    user_input = input('Input your response: ')
    response = change_case(user_input)
    output = response, compare_response(character_name, response), 'Score: ' + str(add_score(character_name, response))
        
    return output


def run_chat(character_list):
    """Runs the chatbot.
    Allows the game in play_game() to run multiple times. Runs infinitely until user inputs 'QUIT'.
    
    Parameters
    ----------
    character_list : list
        A list of Marvel characters.
    
    Returns
    -------
    None
    """

    chat = True
    while chat:
                
        result = play_game(character_list)
        print()
        print(result[1]) # tells player if they are correct or incorrect
        print(result[2]) # displays updated score
        print('-----')

        # ends chat
        if result[0] == 'QUIT': # if user typed 'QUIT' into the chatbot input
            chat = False