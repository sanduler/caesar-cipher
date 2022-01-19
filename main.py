# Name:  Ruben Sanduleac
# Date: January 17, 2022
# Discription:

# list of the letters in the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

# This is function called 'encrypt' that takes the 'text' and 'shift' as inputs. Then, inside the 'encrypt'
# function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt" How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list


def encrypt(plain_text, shift_amount):
    cypher_text = ""
    for letter in plain_text:
        # determine the position of the letter in the alphabet
        position = alphabet.index(letter)
        # determine the position of the letter after the shift amount is acounted for
        new_position = position + shift_amount
        # determine a new position if the position is greater than the amount of letters
        if new_position > 25:
            # acounted for the index[0]
            new_position = new_position - 26
        # find the new letter
        new_letter = alphabet[new_position]
        # add to the black cypher text
        cypher_text += new_letter
    # print the cipher text
    print(f"The encoded text is {cypher_text}")


def decrypt(plain_text, shift_amount):
    cypher_text = ""
    for letter in plain_text:
        # determine the position of the letter in the alphabet
        position = alphabet.index(letter)
        # determine the position of the letter after the shift amount is acounted for
        new_position = position - shift_amount
        # determine a new position if the position is greater than the amount of letters
        # zebra ejgwf, e = 5, 5 - 5 = -1
        if new_position < 0:
            # acounted for the index[0]
            new_position = 26 + new_position
        # find the new letter
        new_letter = alphabet[new_position]
        # add to the black cypher text
        cypher_text += new_letter
    # print the cipher text
    print(f"The encoded text is {cypher_text}")


# Calls the encrypt function and pass in the user inputs. Be able to test the code and encrypt a message.
if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(plain_text=text, shift_amount=shift)
else:
    print("Unknown direction, use encrypt or decrypt")

# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
