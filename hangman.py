import random
import string
word= 'blue green yellow black brown red'.split()
def chooseWord(word):
    return random.choice(word)
def isWordGuessed(secretWord, letterGuessed):
    """
       letterGuessed : the letter which we are guessing
       if all the letter which we are guessing is in secretWord
       then our function  return True otherwise False   
    """
    for x in range(len(secretWord)):
        counter=0
        if secretWord[x] in letterGuessed:
            counter+=1
        if counter == len(secretWord):
            return True
        else:
            return False
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    value = ''
    string = ''
    for char in secretWord:
        if char in lettersGuessed:
            value = char + ' '
        else:
            value = "_ " 
        string = string + value        
    return string
def getAvailableWord(letterGuessed):
    '''
    return the available letter which are not guessed by the user
    '''
    lowerstr=string.ascii_lowercase
    value = ''
    total=''
    for x in lowerstr:
        if x not in letterGuessed:
            value = x
        else:
            value=''
        total=total +value
    return total
def hangman(secretWord):
    guessLeft=8
    letterGuessed=[]
    print('WELCOME to the Game, HANGMAN')
    print('I am thinking of a word that is', str(len(secretWord)), 'long')
    print('--------------------------------------------------------------------')
    
    while guessLeft>0 and not isWordGuessed(secretWord,letterGuessed):
        print('number of guesses left', str(guessLeft))
        print('Available letter are :', getAvailableWord(letterGuessed))
        guess=input('Please guess the letter:  ')
        guess=guess.lower()
        while guess!=1 and guess not in string.ascii_lowercase:
            print('Enter a valid letter')
        if guess not in letterGuessed:
            letterGuessed.append(guess)
            if guess in secretWord:
                print('Good choice')
                
            else:
                guessLeft-=1
                print('WRONG GUESS')
        else:
            print('You have already guess the letter')
        print(getGuessedWord(secretWord,letterGuessed))
    if isWordGuessed(secretWord,letterGuessed):
        print('CONGRATS!!!!!!!!!! You won')
    else:
        print('You LOSS \n You ran out of guess, The word is :', str(secretWord))
        
secretWord=chooseWord(word).lower()
hangman(secretWord)

                
            
                