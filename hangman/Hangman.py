#For beautiful lines: https://www.christianlehmann.eu/sonderzeichen/?open=linien
import os
import random

word = ""
stage = 0
guessed = []
dub =[]

def checker():
    for i in list(word):
        if i in guessed:
            x = 1
        else:
            print(i)
            return True
    return False

def hangman():
    global stage
    match stage: 
        case 0:
            print("         \n         \n         \n         \n         \n         \n          \n\n")
        case 1:
            print("         \n         \n         \n         \n         \n         \n┌────────┐\n\n")
        case 2:
            print("         \n        │\n        │\n        │\n        │\n        │\n┌───────┴┐\n\n")
        case 3:
            print("    ────┐\n        │\n        │\n        │\n        │\n        │\n┌───────┴┐\n\n")
        case 4:
            print("   ┌────┐\n   │    │\n        │\n        │\n        │\n        │\n┌───────┴┐\n\n")
        case 5:
            print("   ┌────┐\n   │    │\n   O    │\n        │\n        │\n        │\n┌───────┴┐\n\n")
        case 6:
            print("   ┌────┐\n   │    │\n   O    │\n   │    │\n        │\n        │\n┌───────┴┐\n\n")
        case 7:
            print("   ┌────┐\n   │    │\n   O    │\n  ╱│╲   │\n  ╱ ╲   │\n        │\n┌───────┴┐\n\n")

def guessing():
    global stage
    global word
    guess = input("Guess a letter: ")
    if guess in word:
        guessed.append(guess)
    else:
        dub.append(guess)
        stage +=1

def hints():

    print("\n")
    for i in dub:
        print(i, end=' ')
    print ("\n")
    
    for i in word:
        if i in guessed:
            print(i, end=' ')
        else:
            print("_", end=' ')
    print()
    
def main():
    global stage
    global word
    print("Let's play Hangman")
    word = input("Write your own Word or simply hit enter for a random one: ").lower()
    if word == "" or word == "\n":
        selection = ['essentially', 'exmatriculation','highway','computer','smartphone']
        word = selection[random.randrange(0,len(selection))]
    run = True
    while stage != 7 and run == True:
        os.system("clear")
        print("Let's play Hangman")
        hangman()
        hints()
        guessing()
        run = checker()
    os.system("clear")
    hangman()
    print("Word: " + word)

    #checks if logs.svd exists and creats it if neccessary
    if not os.path.isfile('logs.svd'):
        f = open('logs.svd', 'w')
        f.write(' Result: Stage: Word:')
        f.close()

    #saves the results in a file
    f = open('logs.svd', 'r')
    old = f.read()
    f.close
    f = open('logs.svd', 'w')
    print("Hooray! You ", end='')
    if stage == 7:
        print("lost.")
        f.write(old + '\n' + 'loosing ' +str(stage) + '      ' + word)
    else:
        print("won.")
        f.write(old + '\n' + 'winning ' + str(stage) + '      ' + word)
    f.close

if __name__ == "__main__":
    main()

