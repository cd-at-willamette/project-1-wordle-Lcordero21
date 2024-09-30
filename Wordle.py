########################################
# Name: Lola Cordero
# Collaborators (if any): Went to the Quad Center for milestone 0
# GenAI Transcript (if any):
# Estimated time spent (hr): 9-10
# Description of any added extensions:
########################################

from WordleGraphics import   WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import ENGLISH_WORDS, is_english_word
import random


def wordle():
    # The main function to play the Wordle game.

    def enter_action():
        if (len(guess(gw.get_current_row())) < 5) and (check_if_english() == True):
            gw.show_message("Word must be at least 5 letters!") #This is will check to make sure word is more then 5 letters
        if check_if_english() == False:
            gw.show_message("Not in Word List Buddy-ol-pal") #This will make sure that the word is in the english list
        else:
            color_squares(guess(gw.get_current_row()))
            check_if_won(guess(gw.get_current_row())) #If guess meets criteria then it will proceed
            gw.set_current_row(gw.get_current_row()+1)                

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    def randomWord():
        random.shuffle(ENGLISH_WORDS)
        word=ENGLISH_WORDS[0]
        while len(word) != N_COLS:
            random.shuffle(ENGLISH_WORDS)
            word=ENGLISH_WORDS[0]
        return word
    
    secretWord = randomWord()
    print (secretWord)

    def check_if_english():
        guess_str= guess(gw.get_current_row())
        guess_lower= guess_str.lower()
        status=False
        for i in range(len(ENGLISH_WORDS)):
            if guess_lower==ENGLISH_WORDS[i]:
                status=True
        return status
    
    def guess(row):
        temp=""
        for i in range(N_COLS):
            temp= temp + gw.get_square_letter(row,i)
        return temp.lower()
    
    def color_squares(guess):
        lettersLeft= secretWord.lower()
        for i in range (N_COLS):
            if guess[i] == lettersLeft[i]:
                lettersLeft= lettersLeft.replace(guess[i], "_", 1)
                gw.set_square_color(gw.get_current_row(),i, CORRECT_COLOR)

        for i in range (N_COLS):
            if gw.get_square_color(gw.get_current_row(),i) != CORRECT_COLOR:
                if guess[i] in lettersLeft:
                    lettersLeft= lettersLeft.replace(guess[i], "_", 1)
                    gw.set_square_color(gw.get_current_row(),i, PRESENT_COLOR)
                else:
                    gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)
        color_keys()

    def check_if_won(guess):
        if gw.get_current_row() == N_ROWS-1:
            if guess == secretWord.lower():
                gw.show_message("You won! Congratulations")
            else:
                gw.show_message("You'll get it next time! The word was: " + secretWord)

        if guess == secretWord.lower():
            gw.show_message("You won! Congratulations")
            gw.set_current_row(N_ROWS)

        
            
    def color_keys():
        for i in range (N_COLS):
            if gw.get_key_color(gw.get_square_letter(gw.get_current_row(),i)) != (CORRECT_COLOR):
                if gw.get_square_color(gw.get_current_row(),i) == CORRECT_COLOR:
                    gw.set_key_color(gw.get_square_letter(gw.get_current_row(),i), CORRECT_COLOR)
                if gw.get_square_color(gw.get_current_row(),i) == PRESENT_COLOR:
                    gw.set_key_color(gw.get_square_letter(gw.get_current_row(),i), PRESENT_COLOR)
                if (gw.get_square_color(gw.get_current_row(),i) == MISSING_COLOR) and (gw.get_key_color(gw.get_square_letter(gw.get_current_row(),i))==UNKNOWN_COLOR):
                    gw.set_key_color(gw.get_square_letter(gw.get_current_row(),i), MISSING_COLOR)
        


     

# Startup boilerplate
if __name__ == "__main__":
    wordle()
