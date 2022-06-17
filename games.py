import guessing.guessing as guessing
import hangman.hangman as hangman   

def choose_game():
    print("*******************************")
    print("*******Choose your game!*******")
    print("*******************************")

    print("(1) - Guessing Game")
    print("(2) - Hangman Game")

    game = int(input("Choose your game: "))

    if(game == 1):
        print("Playing Guessing Game")
        guessing.play()
    elif(game == 2):
        print("Playing Hangman Game")
        hangman.play()

if(__name__ == "__main__"):
    choose_game()