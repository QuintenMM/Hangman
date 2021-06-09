import random



class Hangman:
    def __init__(self, possible_words, word_to_find, lives, correctly_guessed_letters, wrongly_guessed_letters,
                 turn_count, error_count):
        self.possible_words = possible_words
        self.word_to_find = word_to_find
        self.lives = lives
        self.correctly_guessed_letters = correctley_guessed_letters
        self.wrongly_guessed_letters = wrongley_guessed_letters
        self.turn_count = turn_count
        self.error_count = error_count
        self.guess_word = guess_word


def start_game():
    # list of possible words to choose from
    possible_words = ["lemon", "mango", "banana", "apple", "dependent", "field", "equable", "shy", "sheet", "wise",
                      "familiar", "rose", "frighten", "fragile", "amusing", "reaction", "becode", "learning",
                      "mathematics", "sessions"]


    # list to store the wrong letters in
    wrongly_guessed_letters = []

    # a list to store the guessed letters in
    correctly_guessed_letters = []

    # pick a random words from the list
    word_to_find = random.choice(possible_words)
    the_word = list(word_to_find)

    # turn count/ error count

    # for the length of the word to find we print _ to show how many letters
    guessed_word = []
    for i in range(len(word_to_find)):
        guessed_word.append("_")
    print(*([i for i in guessed_word]))
    print(word_to_find)

    lives = 5
    while lives:
        error_count = len(wrongly_guessed_letters)+1
        turn_count = error_count + len(correctly_guessed_letters)
        # take input from user
        guessed_letter = input("What letter do you pick? ")
        # check if guessed_letter is an alphabet
        # just a-z no special numbers
        if not guessed_letter.isalpha():
            print('Guess a letter only, no special symbols or more letters')
        # check if guessed letter length is one or not
        elif len(guessed_letter) > 1:
            print('One letter only. learn the rules omg')
        # check that letter chosen by user is already guessed or not
        elif guessed_letter in wrongly_guessed_letters:
            print("Trying a letter again won't work. Pick another one")
            # check if guessed_letter is matches with word_to_find

        if guessed_letter in word_to_find:
            for i in range(len(word_to_find)):
                if word_to_find[i] == guessed_letter:
                    guessed_word[i] = word_to_find[i]
                    correctly_guessed_letters.append(guessed_word[i])
                    guessed_word[word_to_find.index(guessed_letter)] = guessed_letter
                    print(*([i for i in guessed_word]))
                    print("well done that's a letter found")
        else:
            print("You chose the wrong letter")
            wrongly_guessed_letters.append(guessed_letter)
            lives = lives - 1

        guess_word = [i for i in guessed_word]
        guess_word = "".join(guess_word)

        if word_to_find == guess_word:
            print("Good boy. Here is a coockie!")
            exit(0)
        print(f"You have {lives} lives left")
        if lives == 0:
            if word_to_find  != guessed_word:
                print(f"you wasted your lives. now there is nothing left but Game Over."
                      f" You should have tried {word_to_find}")


if __name__ == '__main__':
    main()