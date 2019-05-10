# BALL PICKER v0.5
# Author: Lucas Geurtjens (s5132841)
# Date: 10/05/2019

import math
import random


# We create a class for storing the ball objects.
class Ball:
    def __init__(self, value, status):
        self.value = [value, rusty_value(value)]  # [0] Scott's value, [1] Rusty's value
        self.status = status  # Has the ball been picked or not?


# Max Heap
"""
Helper Functions:
    - Get an index (parent, left or right child)
    - Check if that index is valid
    - Grab value from that index
    - Swapping the values of two indexes
"""


def get_left(parent_index):
    return 2 * parent_index + 1


def get_right(parent_index):
    return 2 * parent_index + 2


def get_parent(child_index):
    return math.floor((child_index - 1) / 2)


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

    # While we have a parent node and our current value is greater than it
    while parent_exists(index) and balls[index].value[player] > parent(index, balls):

        # CHECK IF PARENT = CHILD
        # Then compare with actual value
        # Only do for rusty

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

        # If we have a right child and it's bigger -> right is largest child
        if right_exists(index, balls) and right(index, balls) > left(index, balls):
            largest_child = get_right(index)

        # For rusty only, check if the values are equal, if so, compare the real values to see which was bigger
        elif player == 0 and right_exists(index, balls) and right(index, balls) == left(index, balls):
            if balls[get_right(index)].value[0] > balls[get_left(index)].value[0]:
                largest_child = get_right(index)

        # If we are bigger than the largest child -> we're in the right spot.
        if balls[index].value[player] > balls[largest_child].value[player]:
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


def game(ball_size, round_turns, ball_list):
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

    # Decide who plays first
    rusty_first = bool(random.getrandbits(1))

    # Rusty is first
    if rusty_first:
        print("Rusty is first")
        while ball_size != 0:

            player = 1
            for _ in range(round_turns):  # For rounds, pop and add root to the score
                score[1] += pop_ball(rusty_b).value[player]
                ball_size -= 1

                if ball_size == 0:  # Did we use all the balls?
                    break

            if ball_size == 0:  # Did we use all the balls?
                break

            player = 0
            for _ in range(round_turns):  # For rounds, pop and add root to the score
                score[0] += pop_ball(scott_b).value[player]
                ball_size -= 1

                if ball_size == 0:  # Did we use all the balls?
                    break

    # Scott is first
    else:
        print("Scott is first")
        while ball_size != 0:

            player = 0
            for _ in range(round_turns):  # For rounds, pop and add root to the score
                score[0] += pop_ball(scott_b).value[player]
                ball_size -= 1

                if ball_size == 0:  # Did we use all the balls?
                    break

            if ball_size == 0:  # Did we use all the balls?
                break

            player = 1
            for _ in range(round_turns):  # For rounds, pop and add root to the score
                score[1] += pop_ball(rusty_b).value[player]
                ball_size -= 1

                if ball_size == 0:  # Did we use all the balls?
                    break

    return score


my_ball_size = 4
my_round_turns = 2
my_ball_list = [32, 23, 1, 32]

game_score = game(my_ball_size, my_round_turns, my_ball_list)
print("Scott:", game_score[0])
print("Rusty:", game_score[1])
