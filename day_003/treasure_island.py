
def main():
    """
    This is a really simple flow game (treasure island)
    """
    print('Welcome to treasure island, your mission is to stay alive.')

    choice_1 = input('Type left or right: ').lower()
    if choice_1 == 'right':
        print('Ah ha! Game Over!')
        return 0
    if choice_1 != 'left':
        print('Invalid input! Game Over!')
        return 0

    choice_2 = input('Wait or swim: ').lower()
    if choice_2 == 'swim':
        print('Ah ha! Game Over!')
        return 0
    if choice_2 != 'wait':
        print('Invalid input! Game Over!')
        return 0

    choice_3 = input('Pick a color - red, blue or yellow: ').lower()
    if choice_3 == 'blue':
        print('You did it!!!')
        return 0
    elif choice_3 == 'red' or choice_3 == 'yellow':
        print('Ah ha! Game Over!')
        return 0
    else:
        print('Invalid input! Game Over!')
        return 0

if __name__ == "__main__":
    main()
        