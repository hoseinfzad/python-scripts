import random 
import hangman_word
import hangman_art


def hangman():
    chosen_word = random.choice(hangman_word.word)

    lives = 6

    display = []
    word_length = len(chosen_word)
    for _ in range(word_length):
        display += "_"
    

    end_of_game = False

    while not end_of_game:
        guess = input("guess a letter: ").lower()
        if guess in display:
            print(f"You have already guessed {guess}.")
            
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
            
        print(f"{' '.join(display)}")
        
        if guess not in chosen_word:
            print(f"You guessed {guess}, thats not in the word, you lose a life!")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose")  


        if "_" not in display:
            end_of_game = True
            print("You win")
            
        print(hangman_art.stages[lives])
    
    print(chosen_word)
        
if '__main__' == __name__:
    hangman()