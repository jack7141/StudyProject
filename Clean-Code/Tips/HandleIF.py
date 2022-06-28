import random

"""
CODE SMELL
def place_a_guess(guesses: int, answer: int, player_name: str):
    if guesses > 0:
        print(f'Player {player_name} has {guesses}')

        guess = int(input("guess number"))
        if guess == answer:
            print('O')
            return True
        else:
            if guess < answer:
                print('Up')
            else:
                print('Down')
            return False
    else:
        return False
"""
def place_a_guess(guesses: int, answer: int, player_name: str):
    if guesses <= 0:
        return False

    print(f'Player {player_name} has {guesses}')
    guess = int(input("guess number"))

    if guess == answer:
        print('O')
    elif guess < answer:
        print('Up')
    else:
        print('Down')
    return guess == answer

def main():
    guesses = 5
    answer = random.randint(1,10)
    name = 'test'
    while guesses > 0:
        if place_a_guess(guesses, answer, name):
            break
        guesses -= 1

if __name__ == '__main__':
    main()