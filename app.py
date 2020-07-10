secret = "captain"
guess = ""

guess_number = 0
guess_limit = 3
out_of_guesses = False

while guess != secret and not(out_of_guesses):

    if guess_number < guess_limit:
        guess = input("Enter guess: ")
        guess_number += 1
    else: 
        out_of_guesses = True

if out_of_guesses:
    print("You are out of guesses, START OVER!!")
else:
    print ("You Win!!!")