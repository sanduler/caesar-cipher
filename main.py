# Name:  Ruben Sanduleac
# Date: January 17, 2022
# Discription:

# list of the letters in the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# 1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# 2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

# How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# Bug alert:  'civilization'

# 3: Call the encrypt function and pass in the user inputs. Be able to test the code and encrypt a message.
