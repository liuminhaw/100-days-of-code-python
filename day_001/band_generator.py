
def main():
    """
    Generate a band name by prompted answer
    """
    #1. Create a greeting for your program.
    print('Hello, this is band generator\n')

    #2. Ask the user for the city that they grew up in.
    city = input('Which city do you grew up in?\n')

    #3. Ask the user for the name of a pet.
    pet = input('What is the name of your pet?\n')

    #4. Combine the name of their city and pet and show them their band name.
    print("Band name: {} {}".format(city, pet))

    #5. Make sure the input cursor shows on a new line, see the example at:
    #   https://band-name-generator-end.appbrewery.repl.run/


if __name__ == '__main__':
    main()
