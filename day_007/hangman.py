import random
import hangman_art
import hangman_words


def main():
    """
    Playing hangman game
    """
    lives = 6
    end_of_game = False
    chosen_word = random.choice(hangman_words.word_list)
    duplicate_test = dict()

    # Print logo
    print(hangman_art.logo)

    #Testing code
    # print(f'Pssst, the solution is {chosen_word}.')

    display = ['_'] * len(chosen_word)
    print(f"display before guess: {' '.join(display)}")

    while not end_of_game:
        guess = input('Guess a letter: ').lower()

        # Test input duplicate
        if guess in duplicate_test:
            print(f'{guess} had already been guessed, try other alphabet')
            continue
        duplicate_test[guess] = True

        for index, letter in enumerate(chosen_word):
            if guess == letter:
                display[index] = guess

        if guess not in chosen_word:
            print(f'Oops, you guessed {guess}, which does not appear in the word.')
            lives -= 1
            print(hangman_art.stages[lives])
            if lives == 0:
                end_of_game = True
                print(f'You lose, the answer is {chosen_word}')

        if '_' not in display:
            end_of_game = True
            print('You win')

        print(f"display after guess: {' '.join(display)}")


if __name__ == "__main__":
    main()
