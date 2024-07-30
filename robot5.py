counter = 0


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():

    if counter == 5:
        build_wall()
    if front_is_clear():
        move()
        counter += 1

    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()

    return counter