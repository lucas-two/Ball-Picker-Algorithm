# BALL PICKER v1.0
# Author: Lucas Geurtjens (s5132841)
# Date: 10/05/2019

import math
import os
import sys


# We create a class for storing the ball objects.
class Ball:
    def __init__(self, value, status):
        self.value = [value, rusty_value(value)]  # [0] Scott's value, [1] Rusty's value
        self.status = status  # Has the ball been picked or not?


# Functions for locating index of parent, left and right child
def get_left(parent_index):
    return 2 * parent_index + 1


def get_right(parent_index):
    return 2 * parent_index + 2


def get_parent(child_index):
    return math.floor((child_index - 1) / 2)


# Functions for checking if the index of parent, left or right child exists
def left_exists(index, balls):
    if get_left(index) < len(balls):  # Check if ball count is exceeded (doesn't exist)
        return True
    return False


def right_exists(index, balls):
    if get_right(index) < len(balls):
        return True
    return False


def parent_exists(index):
    if get_parent(index) < 0:  # Ball count is exceeded (goes into -/ves, hence doesn't exist)
        return False
    return True


# Functions for grabbing the value at the given index
def left(index, balls):
    return balls[get_left(index)].value[player]


def right(index, balls):
    return balls[get_right(index)].value[player]


def parent(index, balls):
    return balls[get_parent(index)].value[player]


def swap(i, j, balls):
    balls[i], balls[j] = balls[j], balls[i]


def add_ball(ball, balls):
    """
    Adds a ball to the heap
    """
    balls.append(ball)  # Add the ball as a leaf
    heapify_up(balls)  # Heapify up


def pop_ball(balls):
    """
    Removes a ball from the heap
    """
    # Check if no balls are left
    if len(balls) == 0:
        print("ERROR, NO MORE BALLS")
        return

    swap(0, len(balls) - 1, balls)  # Swap root and right most leaf node
    root = balls.pop(len(balls) - 1)  # Pop the root (now leaf) node
    heapify_down(balls)  # Heapify down

    if root.status is False:  # If this node has already been taken
        root = pop_ball(balls)  # Pop the next ball instead

    root.status = False  # We've used this ball now

    return root


def heapify_up(balls):
    """
    Take our last index (perhaps just added),
    then bring it up to where it belongs.
    """

    index = len(balls) - 1  # Look at the right most leaf node

    while parent_exists(index):

        # (For Rusty Only)
        # If the index node and parent are equal... Check which is bigger by comparing against true value
        if player == 1 and balls[index].value[player] == parent(index, balls):
            if balls[index].value[0] < balls[get_parent(index)].value[0]:  # If the parent is larger than the child
                break  # Stop

        elif balls[index].value[player] <= parent(index, balls):  # If the child is less or equal to the parent
            break  # Stop

        swap(get_parent(index), index, balls)  # Swap the parent and current index
        index = get_parent(index)  # Set the index to the location of its parent


def heapify_down(balls):
    """
    Compare the root node to its children until it
    is in the correct place.
    """
    index = 0  # Look at the root node

    # While we have children (Since it's a heap, we always have left child first)
    while left_exists(index, balls):

        largest_child = get_left(index)  # Assume left is largest child

        # (For Rusty Only)
        # If right and left are equal... Check which is bigger by comparing against true value
        if player == 1 and right_exists(index, balls) and right(index, balls) == left(index, balls):
            if balls[get_right(index)].value[0] > balls[get_left(index)].value[0]:
                largest_child = get_right(index)

        # If we have a right child and it's bigger -> right is largest child
        elif right_exists(index, balls) and right(index, balls) > left(index, balls):
            largest_child = get_right(index)

        # (For Rusty Only)
        # If they are equal... Stop if the true value of our index is bigger than the largest child
        if player == 1 and balls[index].value[player] == balls[largest_child].value[player]:
            if balls[index].value[0] > balls[largest_child].value[0]:
                break
            else:
                swap(index, largest_child, balls)
                index = largest_child

        # If our ball is bigger than the largest child ball, we must be in the right spot
        elif balls[index].value[player] > balls[largest_child].value[player]:
            break

        # Otherwise, swap with the largest child
        else:
            swap(index, largest_child, balls)
            index = largest_child


def init_balls(balls):
    """
    Initialise a set of ball objects
    """
    ball_obj_list = []  # List containing ball objects

    ball_status = True  # Default status for initialised balls

    # Create a list of ball objects with a value and status
    for ball_value in balls:
        ball_obj = Ball(ball_value, ball_status)
        ball_obj_list.append(ball_obj)

    return ball_obj_list


def rusty_value(ball_value):
    """
    Calculates the value of Rusty's ball based on the
    sum of integers in the value
    """
    total = 0

    ball_value_str = str(ball_value)  # Convert the integer to a string

    # Go though all "letters" of the integer string
    for num in ball_value_str:
        total += int(num)  # Add them to the total

    return total


def game(ball_size, round_turns, ball_list, starting_player):
    """
    Run though a game of ball picking
    """
    global player
    score = [0, 0]  # Stores the total score of scott and rusty ([0] Scott, [1] Rusty)

    ball_objects = init_balls(ball_list)  # Initialise a list of ball objects

    # Initialise Scott's heap
    player = 0
    scott_b = []
    for ball in range(len(ball_objects)):
        add_ball(ball_objects[ball], scott_b)

    # Initialise Rusty's heap
    player = 1
    rusty_b = []
    for ball in range(len(ball_objects)):
        add_ball(ball_objects[ball], rusty_b)

    rusty_first = starting_player  # Who is playing first?

    # Rusty is first
    if rusty_first:
        while ball_size != 0:

            player = 1
            for _ in range(round_turns):  # For rounds, pop and add root to the score
                score[1] += pop_ball(rusty_b).value[0]
                ball_size -= 1

                if ball_size == 0:  # Did we use all the balls?
                    break

            if ball_size == 0:  # Did we use all the balls?
                break

            player = 0
            for _ in range(round_turns):  # For rounds, pop and add root to the score
                score[0] += pop_ball(scott_b).value[0]
                ball_size -= 1

                if ball_size == 0:  # Did we use all the balls?
                    break

    # Scott is first
    else:
        while ball_size != 0:

            player = 0
            for _ in range(round_turns):  # For rounds, pop and add root to the score
                score[0] += pop_ball(scott_b).value[0]
                ball_size -= 1

                if ball_size == 0:  # Did we use all the balls?
                    break

            if ball_size == 0:  # Did we use all the balls?
                break

            player = 1
            for _ in range(round_turns):  # For rounds, pop and add root to the score
                score[1] += pop_ball(rusty_b).value[0]
                ball_size -= 1

                if ball_size == 0:  # Did we use all the balls?
                    break

    return score


def main():
    """
    Main of the program
    """
    try:
        abs_location = os.path.abspath(sys.argv[1])  # Location of input file

    except IndexError:
        print("Error: Program must be run from the commandline with arguments.")
        sys.exit(-1)

    try:
        input_f = open(abs_location, "r")

    except FileNotFoundError:
        print("Error: It appears that the input text file location (absolute location) was incorrect.")
        print("       Try using 'input.txt.txt' in the file path if input.txt did not work.")
        sys.exit(-1)

    test_cases = int(input_f.readline())

    for _ in range(test_cases):

        my_ball_size, my_round_turns = input_f.readline().split()
        my_ball_list = input_f.readline()
        my_coin_toss = input_f.readline().strip()

        my_ball_size = int(my_ball_size)
        my_round_turns = int(my_round_turns)
        my_ball_list = my_ball_list.split()
        my_ball_list = [int(ball) for ball in my_ball_list]  # Convert the strings -> Integers
        my_toss_result = True

        if my_coin_toss == "HEADS":
            my_toss_result = False

        game_score = game(my_ball_size, my_round_turns, my_ball_list, my_toss_result)
        print("%s %s" % (game_score[0], game_score[1]))


if __name__ == "__main__":
    main()
