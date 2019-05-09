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
    return round((child_index - 1) / 2)


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
    return balls[get_left(index)]


def right(index, balls):
    return balls[get_right(index)]


def parent(index, balls):
    return balls[get_parent(index)]


def swap(i, j, balls):
    temp = balls[i]
    balls[i] = balls[j]
    balls[j] = temp
    return balls


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

    swap(0, len(balls) - 1, balls)  # Swap root and right most leaf node
    root = balls.pop(len(balls) - 1)  # Pop the root (now leaf) node
    heapify_down(balls)  # Heapify down

    return root


def heapify_up(balls):
    """
    Take our last index (perhaps just added),
    then bring it up to where it belongs.
    """
    # IMPLEMENTATION: Note, we will need to adjust the 'values' in this part to account
    # for rusty and scott's different value systems

    index = len(balls) - 1  # Look at the right most leaf node

    # While we have a parent node and our current value is greater than it
    while parent_exists(index) and parent(index, balls) < balls[index]:

        parent_index = get_parent(index)  # Grab the parent index
        swap(parent_index, index, balls)  # Swap the parent and current index
        index = parent_index  # Set the index to the location of its parent


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

        # If we are bigger than the largest child -> we're in the right spot.
        if balls[index] > balls[largest_child]:
            break

        # Otherwise, swap with the largest child
        else:
            swap(index, largest_child, balls)
            index = largest_child

    return balls


scott_b = []
add_ball(2, scott_b)
add_ball(4, scott_b)
add_ball(1, scott_b)
add_ball(8, scott_b)
add_ball(9, scott_b)
add_ball(30, scott_b)
add_ball(200, scott_b)
add_ball(3, scott_b)
print(scott_b)

temp = pop_ball(scott_b)
print(scott_b, temp)

temp = pop_ball(scott_b)
print(scott_b, temp)

temp = pop_ball(scott_b)
print(scott_b, temp)

temp = pop_ball(scott_b)
print(scott_b, temp)

temp = pop_ball(scott_b)
print(scott_b, temp)

temp = pop_ball(scott_b)
print(scott_b, temp)

temp = pop_ball(scott_b)
print(scott_b, temp)

temp = pop_ball(scott_b)
print(scott_b, temp)

# Add some kind of checking for if we've reached end of balls...


