#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: May 26, 2021
# This program uses loops to make the random number
# guessing more interresting


# importing the module that makes this work
import random


# main function
def main():
    # vars
    random_num = random.randint(0, 10)

    # main loop
    while True:
        # get the users guess
        user_num_str = input("Guess the random number: ")

        # make sure the users num can be an integer
        try:
            # make sure they inputed a number
            user_num = int(user_num_str)

            # if the number is not between the accepted numbers
            if (user_num < 0 or user_num > 10):
                print("that number is not between 0 and 10")
            else:

                # if they were right
                if (user_num == random_num):
                    print("{} was the correct answer".format(user_num))
                    play_again = input("Play again? (y/n): ")

                    # if they want to play again or not
                    if (play_again == 'y' or play_again == 'Y'):
                        main()
                    else:
                        # say thanks
                        print("Thanks for playing")
                    # break the loop if they decide not to play again
                    # if the ask to play again wasnt here then it would
                    # break out of the loop when the user guessed the
                    # correct answer.
                    break

                # if they were wrong
                else:
                    print("sorry {} was incorrect".format(user_num))

        except ValueError:
            print("Not valid input")


if __name__ == "__main__":
    main()
