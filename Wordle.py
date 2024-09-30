########################################
# Name: Lola Cordero
# Collaborators (if any): Went to the Quad Center for milestone 0
# GenAI Transcript (if any):
# Estimated time spent (hr): 11-12
# Description of any added extensions:
########################################

from WordleGraphics import   WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import ENGLISH_WORDS, is_english_word
import random


def wordle():
    # The main function to play the Wordle game.

    def enter_action():
        if (len(guess(gw.get_current_row())) < N_COLS):
            gw.show_message("Not in 5-Letter Word List, Buddy-ol-pal!") #This is will check to make sure inputed word is more then 5 letters
        if (check_if_english() == False):
            gw.show_message("Not in 5-Letter Word List, Buddy-ol-pal!") #This will make sure that the word is in the english list
        else:
            color_squares(guess(gw.get_current_row())) #This calls the function that will color the squares accordingly
            check_if_won(guess(gw.get_current_row())) #If guess meets criteria then it will proceed
            gw.set_current_row(gw.get_current_row()+1) #This will move on to the next row

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    def randomWord():
        random.shuffle(ENGLISH_WORDS) #randomly shuffles "ENGLISH_WORDS" list
        word=ENGLISH_WORDS[0] # sets vaariable "word" equal to the first word 
        while len(word) != N_COLS: # While the chosen "word" isn't equal to 5 letters it will do the following:
            random.shuffle(ENGLISH_WORDS)# 1.Randomly shuffe "ENGLISH_WORDS"
            word=ENGLISH_WORDS[0] #2.Sets "word" equal to the the first word in the 
        return word #returns our random word that meets requirements
    
    secretWord = randomWord() #Sets our secret word (that we are trying to solve for)
    print (secretWord) 

    def check_if_english():
        guess_str= guess(gw.get_current_row())
        status=False
        for i in range(len(ENGLISH_WORDS)):
            if guess_str==ENGLISH_WORDS[i]:
                status=True
        return status
    
    # The "check_if_english" function will use the function "guess" to get the word that the player entered
    # then compare the guess with all the words in the ENGLISH_WORDS list. It will then set "status" to true if it is an English word.
    # If it is not an english word then "Status" will remain as false. Either way the function will return the value of "Status"
    
    def guess(row):
        temp=""
        for i in range(N_COLS):
            temp= temp + gw.get_square_letter(row,i)
        return temp.lower()
    # This function will just return the player's guess in all lowercase letters
    
    def color_squares(guess):
        lettersLeft= secretWord.lower() #this is how the program keeps track of how many letters are left
        for i in range (N_COLS):
            if guess[i] == lettersLeft[i]: #checks if any letters in player's guess is in the correct spot
                lettersLeft= lettersLeft.replace(guess[i], "_", 1) #if it is, it will "remove" that letter from the "lettersLeft" list
                gw.set_square_color(gw.get_current_row(),i, CORRECT_COLOR) #it will also color that square green

        for i in range (N_COLS):
            if gw.get_square_color(gw.get_current_row(),i) != CORRECT_COLOR: #this checks to see if square has already been assigned a color
                if guess[i] in lettersLeft: # Checks if letter from guess is in the lettersLeft list
                    lettersLeft= lettersLeft.replace(guess[i], "_", 1) #if it IS in the list then the function will delete the letter (once for words that have repeats)
                    gw.set_square_color(gw.get_current_row(),i, PRESENT_COLOR) #this sets that square with the right letter, wrong space, the color yellow
                else:
                    gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR) #All remaining colors will be gray (since they aren't in the solution at all)
        color_keys() #This will go on to color the keys

    def check_if_won(guess):
        if gw.get_current_row() == N_ROWS-1: #if player is on the last row it will check if they have the solution or not
            if guess == secretWord.lower(): 
                gw.show_message("You won! Congratulations") #if player got the correct word this message will appear
            else:
                gw.show_message("You'll get it next time! The word was: " + secretWord.upper()) 
                #if the player got to final guess and doesn't have the correct word, this will display (telling them what the secret word was)

        if guess == secretWord.lower():
            gw.show_message("You won! Congratulations")
            gw.set_current_row(N_ROWS)
            #if player gets correct word before end of guesses, it will display congratulatory message and end the game

        
            
    def color_keys():  #this function is called after every row of guesses
        for i in range (N_COLS):
            if gw.get_key_color(gw.get_square_letter(gw.get_current_row(),i)) != (CORRECT_COLOR): #if letter key isnt already marked as green then the rest will proceed
                if gw.get_square_color(gw.get_current_row(),i) == CORRECT_COLOR:
                    gw.set_key_color(gw.get_square_letter(gw.get_current_row(),i), CORRECT_COLOR) #if square letter is green, then key will be permanently green
                if gw.get_square_color(gw.get_current_row(),i) == PRESENT_COLOR:
                    gw.set_key_color(gw.get_square_letter(gw.get_current_row(),i), PRESENT_COLOR) #if square letter is yellow, then key letter will be yellow
                if (gw.get_square_color(gw.get_current_row(),i) == MISSING_COLOR):
                    gw.set_key_color(gw.get_square_letter(gw.get_current_row(),i), MISSING_COLOR) #if the square letter is marked as gray, then key will be gray
        


     


            



# Startup boilerplate
if __name__ == "__main__":
    wordle()

# Startup boilerplate
if __name__ == "__main__":
    wordle()
