#Venthai Mao
#CSC 110 - Professor Lisa DiPippo
#MASTMIND PROJECT
#DUE MAY 2

import random # import the random module to generate random values

ALL_COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple'] # list of all colors
NUM_COLORS = len(ALL_COLORS)# number of colors 
CODE_LENGTH = 4 # length of the code to be guessed
MAX_GUESSES = 10 # max number of guesses 

# function to generate a random code from ALL_COLORS
def generateCode():
    code = []
    for i in range(CODE_LENGTH):   #loop over the code length of 4
        colorIndex = random.randint(0, NUM_COLORS - 1)  # get a random index within the range of the colors
        code.append(ALL_COLORS[colorIndex]) # Add a color to the code list
    return code

# function to get a guess from the player
def getGuess():
    print("Make a guess of four colors:")
    for i in range(NUM_COLORS):  #loop over number of colors
        print(str(i) + " - " + ALL_COLORS[i], end="\n") 
    print("-----------------------------")
    guess = []
    for i in range(CODE_LENGTH):  #loop over the secret code length
        while True:
            try:
                colorIndex = int(input("Guess color: "))  #error handling if guess a number not in range 
                if colorIndex not in range(NUM_COLORS):
                    print("Invalid guess, try again:")
                    continue
                break
            except ValueError:                           #error handling if guess a letter
                print("Invalid number, try again:")
        guess.append(ALL_COLORS[colorIndex])
    return guess

# function to evaluate a guess and provide feedback
def CheckGuess(guess, code):
    clue = []
    temp_code = code.copy() # make a copy of the code to avoid modifying the originalsecret code
    temp_guess = guess.copy()# make a copy of the guess to avoid modifying the original guess

# check for exact matches and update the clue
    for i in range(CODE_LENGTH):
        if temp_guess[i] == temp_code[i]:
            clue.append(2)
            temp_code[i] = None   # mark the corresponding index as None to avoid counting it again
            temp_guess[i] = None

# check for partial matches and update the clue
    for i in range(CODE_LENGTH):
        if temp_guess[i] is not None and temp_guess[i] in temp_code:
            clue.append(1)
            temp_code[temp_code.index(temp_guess[i])] = None # mark the corresponding index as None to avoid counting it again
            temp_guess[i] = None

    return sorted(clue)   # sort the clue in ascending order

# main function to run the game
def main(seedValue):
    random.seed(seedValue)   # set the seed value for the random number generator
    play_again = "Y"         # initialize the play_again variable to 'Y'
    while play_again == "Y": # loop as long as the player wants to play again
        print("The secret code has been chosen. You have 10 tries to guess the code.")

        code = generateCode()   # generate a new code for each game
        guessesLeft = MAX_GUESSES # set the maximum number of guesses for each game
        guessesTaken = 0         # initialize the number of guesses taken to 0
        while guessesLeft > 0:   # loop as long as there are guesses left
            print("-----------------------------")
            guess = getGuess()   # get a new guess from the player
            print("-----------------------------")
            clue = CheckGuess(guess, code)  # evaluate the guess and get the clue
            print("Your guess is:")
            print(guess)
            guessesTaken += 1        # increment the number of guesses 
            if clue == [2, 2, 2, 2]:
                print("\nCorrect! You finished in ", guessesTaken, "guesses") #tell the player if they made the correct guess
                break
            else:
                print("\nYour clue is:", clue)          #else tells them clues and how many guesses left
                guessesLeft -= 1
                if guessesLeft > 0:
                    print("\nYou have", guessesLeft, "guesses left")

        if guessesLeft == 0:                                #if the player runs out of guesses, it tells them they ran out of guesses and shows the code
            print("\nNo more guesses, the hidden colors were:", str(code))
            
            play_again = input("\nWould you like to play again? (Y/N)").upper()     #ask user to play again

        elif guessesLeft > 0:
            play_again = input("\nWould you like to play again? (Y/N)").upper()    #ask user to play again

    if play_again != "Y":
        print("\nThank you for playing. Good-bye!")      #ends the game if they say N
