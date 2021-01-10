import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def main():
    """
    Encrypt and decrypt input text with caesar cipher
    """
    print(art.logo)
    print('')

    recursive()

def caesar(method, text, shift):
    """
    Using caesar cipher to encrypt / decrypt input text with given shift amount
    """
    result_text = ''

    for char in text:
        if char in alphabet:
            if method.lower() == 'encode':
                index_of_result_char = (alphabet.index(char) + shift) % len(alphabet)
            elif method.lower() == 'decode':
                index_of_result_char = (alphabet.index(char) - shift) % len(alphabet)
            result_text += alphabet[index_of_result_char]
        else:
            result_text += char

    print(f'The {method.lower()}d text is {result_text}')

def recursive():
    """
    Recursively ask user if want to play again
    """
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while direction != 'encode' and direction != 'decode':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)

    again = input('Run caesar cipher again? (yes/no): ').lower()

    if again == 'yes':
        recursive()

if __name__ == '__main__':
    main()
