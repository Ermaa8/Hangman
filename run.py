import random
import string
import sys
import os
import time
from datetime import datetime, date
name = ''
cities = [
    "Amsterdam", "Stckholm", "Peking", "London", "Paris", "Tokyo",
    "Delhi", "MexicoCity", "Cairo", "Berlin", "Mumbai", "Beijing", "Dhaka", "Osaka", "New York", "Karachi",
    "BuenosAries", "Istanbul", "Manila", "RiodeJaneiro", "LosAngeles", "Lima",
    "Bangok", "Seoul", "Teheran", "Chicago", "Chengdu", "Nanjing", "Wuhan", "Luanda",
    "Santiago", "Baghdad", "Damascus", "Pune", "Madrid", "Barcelona", "Harbin", "Surad", 
    "Dallas", "Gothenburg", "Miami", "Toronto", "Hamburg", "Atlanta", "Fukuoka", "Singapore",
    "BeloHorizonte", "Khartoum", "Dalian", "SaintPetersburg", "Alexandria", "Jinan", "Guadalajara",
    "Shangai", "SaoPaulo", "Tianjin", "Lagos", "Kinshasa"
]
countries = [
    "Hungary", "Austria", "Italy", "Brazil", "Japan", "Ireland", "Sweden", "Cuba",
    "NewZeland", "Venezuela", "Colombia", "Chile", "Peru", "Marocco", "Kenya", 
    "Nigeria", "Bangladesh", "Philipines", "Portugal", "Ukraine", "Russia", "Pakistan", "Vietna", "China",
    "Iran", "Norway", "Finland", "Switzerland", "Netherlands", "SouthKorea", "Belgium", 
    "Denmark", "Germany", "Spain", "Croatia", "Bulgaria", "Romania", "Mexico", "Argentina", "SouthAfrica",
    "Poland", "Egypt", "Indonesia", "Greece", "Turkey", "Estonia"
]
flowers = [
    "wisteria", "verbena", "sweetpea", "tigerlily", "peony", "narcissus",
    "rose", "tulip", "daisy", "lily", "peonies", "hydrangea", "poppy", "marigold", "daffodil", "orchid",
    "aster", "lilac", "zinnia", "dahlia", "azalea", "anemone", "cosmos", "fuchsia",
    "pansy", "zinnia", "dahlia", "lavander", "iris", "anemone", "crocus", "hibiscus", "camellia",
    "ranuncuus", "gerbera", "forgetmenot", "azalea"
]
languages = [
    "Punjabi", "Gujarti", "Somali", "Zulu", "English", "Spanish", "Arabic", "Albanian",
    "Slovenian", "French", "German", "Italian", "Portuguese", "Estonian", "Latvian", "Lithuanian", "Tagalog", 
    "Malay", "Ukrainian", "Bulgarian", "Slovak", "Hungarian", "Czech", "Romanian", "Danish", "Norwegian", "Finnish",
    "Turkish", "Thai", "Vietnamese", "Polish", "Greek", "Swedish", "Dutch", "Korean", "Indonesian",
    "Russian", "Japanese", "Chinese", "Hindi", "Bengali", "Urdu"
]
fruits = [
    "gooseberry", "soursop", "kumquat", "ackee", "elderberry", "rhubarb", "honeydew",
    "startfruit", "mandarin", "apple", "pear", "strawberry", "banana", "orange", "grape",
    "peach", "watermelon", "blueberry", "mango", "kiwi", "pineapple", "cherry", "guava", 
    "pomegranate", "cranberry", "blackberry", "kiwifruit", "papaya", "lychee", 
    "coconout", "nectarine", "mulberry", "clementine"
]


categories = {
    "Cities": cities,
    "Countries": countries,
    "Flowers": flowers,
    "Languages": languages,
    "Fruits": fruits
}
levels = {
    "Easy - 8 lives: Perfect for begginers": 8,
    "Hard - 4 lives: For players that seek a challenge": 4
}

def startup_view(): 
    # Plays the startup welcome effect with colors and text effects.
    # Welcome message with slow typing effect using txt_effect
    txt_effect("Welcome to The Hangman!\n\n")
    txt_effect("Prepare yourself for a journey "
               "thrugh the alphabet jungle.\n\n")
    txt_effect("How to play\n")
    txt_effect("\033[91m"
               f"   ______\n"
               f"  |      |\n" 
               f"  |      o\n"
               f"  |     /|\\\n"
               f"  |     / \\\n"
               f"  |\n"
               f"  |\n"
               f"__|________"
               + "\033[0m\n\n")
    print("1. Enter your username. "
           "It must be 3 letters or 3 numbers.")
    print("2. Choose your level.")
    print("3. Select your favorite category.")
    print("4. Start guessing.\n")
    #Allow time for visual impact
    time.sleep(1.5)
    # Print the text with a slower typing
    # Effect and aditional customizations
    # Adjust speed ig needed (lower number means slower typing)

def txt_effect(text_to_print):
    for character in text_to_print:
        time.sleep(0.03)
        sys.stdout.write(character)
        sys.stdout.flush()
    # From:
    # https://stackoverflow.com/questions/2084508/clear-termina-in-python

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_hangman(mistakes, chosen_level):
    hangman_stages = [
        "",
        f"   _______\n"
        f"  |       \n"
        f"  |\n"
        f"  |\n"
        f"  |\n"
        f"  |\n"
        f"  |\n"
        f"__|________",
        f"   _____\n"
        f"  |     |\n"
        f"  |\n"
        f"  |\n"
        f"  |\n"
        f"  |\n"
        f"  |\n"
        f"__|________",
        f"   _____\n"
        f"  |     |\n"
        f"  |     o\n" 
        f"  |     /\n"
        f"  |\n"
        f"  |\n"
        f"  |\n"
        f"__|________",
        f"   _____\n"
        f"  |     |\n"
        f"  |     o\n" 
        f"  |    /|\n"
        f"  |\n"
        f"  |\n"
        f"  |\n"
        f"__|________",
        f"   _____\n"
        f"  |     |\n"
        f"  |     o\n" 
        f"  |    /|\\\n"
        f"  |\n"
        f"  |\n"
        f"  |\n"
        f"__|________",
        f"   _____\n"
        f"  |     |\n"
        f"  |     o\n" 
        f"  |    /|\\\n"
        f"  |    /\n"
        f"  |\n"
        f"  |\n"
        f"__|________",
        f"   _____\n"
        f"  |     |\n"
        f"  |     o\n" 
        f"  |    /|\\\n"
        f"  |    /\\\n"
        f"  |\n"
        f"  |\n"
        f"__|________",
    ]
    # Adjust the rate of displaying hangman stages on the chosen level
    if chosen_level == "Easy - 8 lives: Perfect for beginners":
        display_per_mistake = 1 # Display two stages per mistake
    # Easy level - Display 1 stage per mistake
    # Hard level - Display 2 stage per mistake
    else:
        display_per_mistake = 2
    # Calculate the number of stages to display for the current mistake
    stages_to_display = min(mistakes *
                            display_per_mistake,
                            len(hangman_stages) - 1)
    print("\033[91m" + hangman_stages
          [stages_to_display] + "\"033[0m")
    return stages_to_display

def choose_level():
    startup_view()
    name_is_valid = False
    while name_is_valid is False:
        name = get_user_input("Gamer, your username"
                              "is your secret sauce."
                              "Make it funny!\n")
        clear_terminal()
        name_is_valid = len(name) >= 3
        if name_is_valid is False:
            print("Gimme names, not games!")
            print("\033[91mEnter at least 3 letters \033[0m"
                  "\033[91mor numbers!\033[0m\n")
    print(f"{name}, glad to have you join!")
    print("Ready to teckle some challenging words?\n")
    print("Step 1: Choose"
          "Your Level of Adventure!")
    # Yellow decorative line
    print("\033[1;33;40m" + "_" * 39 + "\033[0m\n")
    for i, level in enumerate(levels):
        print(f"{i+1}. {level}")
    while True:
        print(" ")
        choice = input("Enter level (1-2): ")
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(levels):
                chosen_level = list(levels.keys())[choice]
                clear_terminal()
                print("You selected" + 
                       chosen_level + ".")
                # Yellow decorative line
                print("\033[1;33;40m" + "_" * 58 + "\033[0m\n")
                print(f"\033[92mGreat choice {name}!\033[0m")
                print(" ")
                #chosen_list refers to aa list of words associated
                #with the category that user has chosen to play with.
                chosen_level_lives = levels[chosen_level]
                return chosen_level, chosen_level_lives, name
            else:
                print(" ")
                print("It's too much, try again!")
                print(f"\033[91m{name}, Please enter \033[0m"
                      "\033[91ma number between 1 and 2. \033[0m")
        else:
             print(" ")
             print("Your character sounds like a song.")
             print(f"\033[91m{name}, Please enter a number. \033[0m")

def choose_category(name):
    print("Step 2: Let's explore!")
    # Yellow decorative line
    print("\033[1;33;40m" + "-" * 43 + "\033[0m\n")
    print("What is your favorite category?")
    for i, category in enumerate(categories):
        print(f"{i+1}. {category}")
    input_valid = False
    while input_valid is False:
        choice = input("Enter your choice (1-5): ")
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(categories):
                input_valid = True
                clear_terminal()
                chosen_category = list(categories.keys())[choice]
                print("\033[92mYou selected", chosen_category + ".\033[0m")
                print(" ")
                print("Step 3: Let the game begin!")
                # Yellow decorative line
                print("\033[1;33;40m" + "_" * 36 + "\033[0m\n")
                #Print the category here
                print("On your marks, get set, guess!\n"
                        "The hangman's rope hangs in the balance!")
                # chosen_list refers to a list of words
                # associated with the category that
                # the user has chosen to play with.
                chosen_list = categories[chosen_category]
                return chosen_category, chosen_list
            else:
                print("_")
                print("I see yu're struggling with"
                        "your keyboard skills.")
                print("\033[1mPease enter a number between 1 and 5.\033[0m")
        else:
                print("_")
                print("Is that character part of a secret code?")
                print(f"\033[91m{name}, Please \033[0m"
                        "\033[91menter a number.\033[0m")

def get_user_input(prompt):
    return input(prompt)

def hangman():
    chosen_level, chosen_level_lives, name = choose_level()
    chosen_category, chosen_list = choose_category(name)
    word = chosen_category
    word_letters =set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    mistakes = 0 
    while len(word_letters) > 0 and mistakes < chosen_level_lives:
        display_hangman(mistakes, chosen_level)
        print(" ")
        print('You have', chosen_level_lives - mistakes, 'lives left.')
        # Yellow decorative line
        print("\033[1;33;40m" + "_" * 22 +"\033[0m\n")
        word_list = [f'\033[1;33;40m{letters}\033[0m' if letters in
                        used_letters else '_' for letters in word]
        print('Current word:',''.join(word_list))
        print('Used letters:', ''.join(used_letters))
        print(" ")
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            clear_terminal()
            used_letters.add(user_letter)
            if user_letter in word_letters:
                print("It was Estonia! "
                        "Or maybe a Peru?\n"
                        "\033[92mNo matter, you guessed right!\033[0m")
                word_letters.remove(user_letter)
            else:
                mistakes += 1
                print("\033[91mYikes! Swing and a miss...\033[0m")
        elif user_letter in used_letters:
            clear_terminal()
            print("\033[91mOopsie!\033[0m That letter's already"
                    "been served.\nLet's do something new!")
        else:
            clear_terminal()
            print("The keyboard just ate your character!")
            print("\033[91mPlease choose a valid \033[0m"
                    "\033[91mone before it attack again.\033[0m")
    if mistakes == chosen_level_lives:
        display_hangman(mistakes, chosen_level)
        print(" ")
        print("\033[91mOh, no!\n\n\033[0m"
                "looks like your brain"
                 "went\non vacation.\n")
        print("\033[91mThe word was", word, "\033[0m")
        print(" ")
    else:
        print(" ")
        print("\033[92mThe word was", word, "\033[0m")
        print(" ")
        print("You guessed it!")
        print(" ")
        print("Your detective skills are\n"
                "Really sharp.")
        print(" ")
        
def continue_game():
    while True:
        print("Ready for another round? (y/n)\n"
                "It's like a chocolate, you can't have just one.")
        choice = input().lower()
        if choice == "y":
            # Assuming you have a clear terminal function defined
            clear_terminal()
            print(" ")
            print(" ")
            print(" Oh good, you have not given"
                    "up yet. This will be interesting...")
            print(" ")
            while True:
                print("Are you as certain as a squirrel "
                        "crossing a busy highway?\n"
                        "better say...\n")
                you_sure = input("Are you sure you're sure? (y/n)\n").lower()
                # Check for both "y" and "n"
                if you_sure in ("y", "n"):
                    if you_sure == "y":
                        clear_terminal()
                        #Assuming you have a hangman function defined
                        hangman()
                        #Exit inner loop on confirmation
                        break
                    elif you_sure == "n":
                        clear_terminal()
                        print(" ")
                        print("Brave soul! Remember,\n"
                                "quitting is good... sometimes.\n")
                        print("Don't tell anyone I said that.")
                        #exit the function, effectively ending the game
                        return
                else:
                    print("\n\033[91mPlease enter \033[0m"
                            "\033[91m'y' or 'n'.\033[0m\n")
        # Handle "n" from the first prompt directly
        elif choice == "n":
                clear_terminal()
                print(" ")
                print("Thanks for playing!")
                # Yellow decorative line
                print("\033[1;33;40m" + "-" * 19 + "\033[0m\n")
                print(" ")
                print("...and please excuse any existential dread")
                print("you may have experienced during the game.")
                print(" ")
                print("I am still learing, after all")
                print(" ")
                # Exit the entire loop after farewell message
                break
        else:
                print(" ")
                print("Wow, that was... something")
                print("trying to speak Morse code?")
                print("\033[91mPlease enter 'y' or 'n'.\033[0m\n")

if __name__ == "__main__":
    hangman()
    continue_game()

        