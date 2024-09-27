########################################
# Name: Lola Corder
# Collaborators (if any): went to QUAD Center
# GenAI Transcript (if any):
# Estimated time spent (hr): 1
# Description of any added extensions:
########################################

from WordleGraphics import   WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import ENGLISH_WORDS, is_english_word
import random


def wordle():
    # The main function to play the Wordle game.
    row=0 
    
    
    def display_word(word):
        for i in range(N_COLS):
            letter=word[i]
            gw.set_square_letter(0,i,letter)

        
    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        gw.show_message("You need to implement this method")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    secret_word="Happy"
    display_word(secret_word)
    

# Startup boilerplate
if __name__ == "__main__":
    wordle()
