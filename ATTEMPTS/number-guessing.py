# Number guessing game - text based
# idea - generate random numbers and help user guess using hint levels
# made by alizan

import random
import math
import time  # for delays

# --- INITIAL SETTINGS ---
difficulty = "Easy"  # starting difficulty
level = 1  # starting level

# --- HELPER FUNCTIONS ---

# get number settings based on difficulty & level
def get_settings(difficulty, level):
    if difficulty.lower() == "easy":
        return 1, 10, 1
    elif difficulty.lower() == "med":
        if level < 15:
            return 1, 50, 2
        else:
            return 1, 100, 3
    elif difficulty.lower() == "hard":
        if level < 55:
            return 5, 180, 5
        else:
            return 6, 500, 6
    else:
        return 1, 10, 1

# generate numbers
def gen_random_numb(count, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(count)]

# messages
wrong_msgs = [
    "Nope! Try again.",
    "Haha, not even close.",
    "Wrong guess, think harder.",
    "Oops, that's off!",
    "You can do better than that!"
]

correct_msgs = [
    "WOW! You got it!",
    "Nice one!",
    "Bingo!",
    "Correct! Level up!",
    "That's it!"
]

# display hints (with option to back out)
def show_hints(numbers):
    while True:
        print("\nHINTS MENU\n")
        print("1 - Hint 1 - minimum number")
        print("2 - Hint 2 - maximum number")
        print("3 - Hint 3 - sum of numbers")
        print("4 - Reveal final numbers")
        print("5 - Go back\n")
        choice = input("=> ").strip()
        print("\n")
        if choice == "1":
            print(f"Hint 1 - minimum number = {min(numbers)}\n")
            time.sleep(1)
        elif choice == "2":
            print(f"Hint 2 - maximum number = {max(numbers)}\n")
            time.sleep(1)
        elif choice == "3":
            print(f"Hint 3 - sum of numbers = {sum(numbers)}\n")
            time.sleep(1)
        elif choice == "4":
            print(f"Final numbers - {numbers}\n")
            time.sleep(1)
        elif choice == "5":
            print("Returning to level menu...\n")
            time.sleep(1)
            break
        else:
            print("Unknown option, pick 1-5\n")
            time.sleep(1)

# --- MAIN GAME LOOP ---
while True:
    # --- START MENU ---
    print("\n" * 2)
    print("WELCOME! To ali's guessing game!!!\n")
    time.sleep(1)
    print("1 - Play")
    print("2 - Settings")
    print("3 - Exit\n")
    choice = input("=> ").strip()
    print("\n")
    time.sleep(0.5)

    if choice == "1":  # PLAY
        while True:
            min_val, max_val, num_count = get_settings(difficulty, level)
            numbers = gen_random_numb(num_count, min_val, max_val)

            # --- LEVEL SCREEN ---
            print("\n" * 2)
            print(f"LEVEL {level}\n")
            time.sleep(1)
            print(f"CLUE - {len(numbers)} numbers present\n")
            time.sleep(1)

            # --- LEVEL OPTIONS ---
            while True:
                print("1 - Guess")
                print("2 - Hints")
                print("3 - Exit to main menu\n")
                cmd = input("=> ").strip()
                print("\n")
                time.sleep(0.5)

                if cmd == "3":  # exit level
                    print("Exiting to main menu...\n\n")
                    time.sleep(1)
                    break

                elif cmd == "2":  # show hints
                    show_hints(numbers)

                elif cmd == "1":  # guess
                    user_input = input("Enter your guess numbers separated by space => ").split()
                    try:
                        user_guess = [int(x) for x in user_input]
                    except ValueError:
                        print("Please enter numbers only.\n\n")
                        time.sleep(1)
                        continue

                    print("\n")
                    time.sleep(0.5)

                    if sorted(user_guess) == sorted(numbers):
                        print(random.choice(correct_msgs) + "\n\n")
                        level += 1
                        time.sleep(1)
                        break  # next level
                    else:
                        print(random.choice(wrong_msgs) + "\n\n")
                        time.sleep(1)

                else:
                    print("Unknown option, pick 1, 2 or 3\n")
                    time.sleep(1)

            if cmd == "3":  # back to start menu
                break

    elif choice == "2":  # SETTINGS
        print("\nChange difficulty?\n1 - Yes\n2 - No\n")
        set_choice = input("=> ").strip()
        print("\n")
        time.sleep(0.5)
        if set_choice == "1":
            print("Choose difficulty:\n1 - Easy\n2 - Med\n3 - Hard\n")
            diff_choice = input("=> ").strip()
            print("\n")
            if diff_choice == "1":
                difficulty = "Easy"
            elif diff_choice == "2":
                difficulty = "Med"
            elif diff_choice == "3":
                difficulty = "Hard"
            else:
                print("Invalid choice, keeping previous difficulty.\n\n")
                time.sleep(1)
                continue
            print(f"Difficulty set to {difficulty}\n\n")
            time.sleep(1)
        else:
            print("No changes, returning to start menu.\n\n")
            time.sleep(1)

    elif choice == "3":  # EXIT
        print("Goodbye! Exiting game...\n\n")
        time.sleep(1)
        break

    else:
        print("Unknown option, pick 1, 2 or 3\n\n")
        time.sleep(1)
