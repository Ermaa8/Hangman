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
    "Poland", "Egypt", "Indonesia", "Greece", "Turkey"
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
categories = {
    "Cities": cities,
    "Countries": countries,
    "Flowers": flowers,
    "Languages": languages
}
levels = {
    "Easy - 8 lives: Perfect for begginers": 8,
    "Hard - 4 lives: For players that seek a challenge": 4
}

def startup_view(): 
    # Plays the startup welcome effect with colors and text effects.
    # Welcome message with slow typing effect using txt_effect
    txt_effect("Welcome to The Hangman!\n\n")
    txt_effect("Prepaare yourself for a journey "
               "thrugh the alphabet jungle.\n\n")
    txt_effect("How to play\n")
    txt_effect("\033[91m"
               f"  ______\n"
               f" |      |\n" 
               f" |      o\n"
               f" |     /|\\\n"
               f" |     / \\\n"
               f" |\n"
               f" |\n"
               f"_|________
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
        f"  |     /\n
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
          [stages_to_display] + \033[0m")
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
                  