import random

class Ball:
    def __init__(self, value, status):
        self.value = value
        self.status = status


def init_heap(ball_list):
    for ball in ball_list:
        Ball(ball[0], True)


# Rusty Picker - He wants the max sum of numbers
def rusty_pick(balls):
    return 0


# Scott Picker - He just wants the largest number
def scott_pick(balls):
    max_ball = balls[0]

    for element in balls:
        if element > max_ball:
            max_ball = element


def game(ball_size, round_turns, ball_list):
    score = []

    # Coin flip on who will play first
    rusty = bool(random.getrandbits(1))

    if rusty:  # Rusty -> Scott

        while ball_size != 0:
            rusty_pick()
            scott_pick()

    else:  # Scott -> Rusty
        while ball_size != 0:
            scott_pick()
            rusty_pick()



# INPUT
# 2 - No of test cases
# 2 1 - No. of balls and no of turns per round
# 1000 99 - Balls

# test_cases = input("Enter No. of Test Cases: ")
# my_test_cases = int(test_cases)
test_cases = 1  # TESTING INPUT

for i in range(test_cases):
    # my_ball_size, my_round_turns = input("Enter Amount of Balls Used and Turns per Round").split()
    # my_ball_list = input("Enter a List of Balls Used")
    #
    # int(my_ball_size)
    # int(my_round_turns)
    # my_ball_list = my_ball_list.split()
    # my_ball_list = [int(ball) for ball in my_ball_list]  # Convert the strings -> Integers

    # TESTING INPUT
    my_ball_size = 3
    my_round_turns = 1
    my_ball_list = [10, 22, 4]

    game_score = game(my_ball_size, my_round_turns, my_ball_list)
