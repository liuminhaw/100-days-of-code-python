
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def main():
    """
    Algorithm for Reeborg's robot to escape the maze
    Reeborg Intro - Maze
    """
    count_turn = 0

    while not at_goal():
        if count_turn == 4:
            if front_is_clear():
                move()
            else:
                turn_left()
            count_turn = 0
        elif right_is_clear():
            turn_right()
            move()
            count_turn += 1
        elif front_is_clear():
            move()
        else:
            turn_left()