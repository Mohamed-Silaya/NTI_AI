import logo
import random 
print(logo.art)

# this function generate int number from 1 to 100 and this what you are tring to get
def random_func():
    """Generates a random integer between 1 and 100."""
    rand_num = random.randint(1, 100)
    return rand_num
# this fuction will receve the game level and send the number of tries
def game_level(level):
    """Returns the number of tries for the given game level."""
    if (level == "easy" or level == "Easy" or level == "E"):
        number_of_tries = 10
        return number_of_tries
    elif (level == "hard" or level == "Hard" or level == "H"):
        number_of_tries = 5
        return number_of_tries
    else :
        raise ValueError("Invalid game level.")
#start from here
def start_game():
    """Starts the number guessing game."""
    level = input("Enter the level Hard or Easy\n")
    number_of_tries=int(game_level(level))
    print("The rand num is generated \n")
    secret_number = random_func()

    # print("Now geuss the number\n")
    for number in range(number_of_tries):
        iter=number_of_tries -number
        print("*************************************")
        print(f"you have {iter} lives remain ")
        print("*************************************")
        y=int(input("guess? : "))
        if y == secret_number:
            print("\n",logo.win)
            break
        elif y < secret_number:
            print("\n***low***")
        elif y > secret_number:
            print("\n***High***")
        if number == number_of_tries-1:
            print(logo.loos)
        



if __name__=="__main__":
    start_game()
