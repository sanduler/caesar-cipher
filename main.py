# Name:  Ruben Sanduleac
# Date: January 17, 2022
# Discription:

from logo import background
print(background)


def caesar(plain_text, shift_amount, cipher_direction):
    cypher_text = ""
    # if the user selects to decode the message
    if cipher_direction == "decode":
        # create a negative shift for decode
        shift_amount *= -1
    for character in plain_text:
        # starts the if statement only if the entered character is in the alphabet
        if character in alphabet:
            # determine the position of the letter in the alphabet
            position = alphabet.index(character)
            # determine the position of the letter in the alphabet then add the shift amount
            new_position = position + shift_amount
            if new_position > 25:
                # acounted for the index[0]
                new_position = new_position - 26
            # find the new letter
            cypher_text += alphabet[new_position]
        # else the character is skipped and added to the cypher text
        else:
            cypher_text += character
    print(f"The {cipher_direction} text is {cypher_text}:\n")


while True:
    # list of the letters in the alphabet
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)
    again = input(
        "Type 'yes' if you want to continue. Otherwise type 'no' to stop.\n").lower()
    if again != 'yes':
        break
