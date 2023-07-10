from assets import list_of_words, title, the_gallows
import random
import os

banner = title
hidden_word = random.choice(list_of_words).lower()
word_in_char = []
is_there_underscore = False
chances_to_live = 6


print(f"\n{banner}\nHey Hero. Time to use that hero brain 🧠 and save the day ✊🏾")

for n in range(len(hidden_word)):
    word_in_char.append("_")

while not is_there_underscore:
    os.system('clear')
    print(f"\nThe secret word is: {''.join(word_in_char)} 🤷🏽‍\n{the_gallows[chances_to_live]}")
    user_guess = input("Guess the letters of the secret word 🤭: ").lower()

    for letter in range(len(hidden_word)):
        if user_guess == hidden_word[letter]:
            word_in_char[letter] = user_guess

    if user_guess not in word_in_char:
        chances_to_live -= 1
        if chances_to_live == 0:
            is_there_underscore = True
            print(f"\n{the_gallows[chances_to_live]}\nYou lost 😞😢😭. The secret word was: ** {hidden_word} **")

    if "_" not in word_in_char:
        is_there_underscore = True
        print(f"\nYou win🎉🍾!!! The secret word is: ** {hidden_word} **")


