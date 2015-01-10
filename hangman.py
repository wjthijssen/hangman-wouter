import random as rand
from hangmangallowsimages import hangmangallows
from findall import find_all

#Need to define the list of words to use
wordlist = open('hangmanwords.txt').read().splitlines()

#Need a random number generator to choose a random word from the list each time the program is run
indexforword = rand.randrange(0,len(wordlist))
word = wordlist[indexforword].lower()
#Hangman images imported from hangmangallowsimages script

##########################The code works up to here#########################################
#Print out user interface with the _ _ _ _ and the hangman gallows drawing
print "Hello and welcome to the Hangman game. Below I'll quickly explain the rules of this particular version."
print "\n\t1. You have to guess the letters of the word you see in '_ _ _ _' characters. A correct guess will display",
print "all\n\t instances of that letter in the word. \n\t2. A wrong guess adds to the Hangman's demise! You can guess",
print "wrong 9 times before the Hangman is complete hung!"
print "\t3. You win if you guess the word fully, lose if the hangman is completely hung"

print "Okay, let's get started!"

userguess = []
for letter in word:
    userguess.append('_')
userguess = ' '.join(userguess)
#Initial user interface asking for a letter

def game(word):
    global userguess
    i = 0
    k = 1
    guesshistory = []
    while i < 8 and True:
        userinterface = [hangmangallows[i], userguess]
        print userinterface[0],'\n' + userinterface[1] + '\n', '\n' + "You have already guessed:" + str(guesshistory)
        #    Decision analysis i.e. is it in the word, and then two branches for right or wrong and the subsequent
        #    effect on the gallows and _ _ _
        print "Please enter your guess number %d" % (k)
        guessi = raw_input('-->' ).lower()
        #    Do some tests on guessi here to see if it's just one letter
        if len(guessi) > 1 or not guessi.isalpha():
            print "Please enter just one letter as a guess"
        elif guessi in guesshistory:
            print "You have already guessed that letter, please enter another guess"
        else:
            if guessi in word:
                print "\n\nYou guessed correctly\n\n"
                wordindices = list(find_all(word,guessi))
                userguesslist = list(userguess)
                for j in wordindices:
                    userguesslist[2*j] = guessi
                    userguess = ''.join(userguesslist)
            else:
                print "\n\nYou guessed wrong! Hangman is one step closer to his end...\n\n"
                i += 1
            k += 1
        if guessi not in guesshistory:
            guesshistory.append(guessi)
        if '_' not in userguess:
            print "the word %r and have guessed correctly enough to have won the game!" % word
            break
    else:
        print "In fact, Hangman has reached his end. Game over! P.S. The word was %r" % word

#Finally, executing the script
game(word)
