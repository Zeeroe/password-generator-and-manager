import random
import string
from random_word import RandomWords
r = RandomWords()

lowers = string.ascii_lowercase
uppers = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

characters = str()
length = int()


def password_inputs():
    global characters
    global length

    length = int(input('password length: '))
    char_input = input('select options: ')

    if 'l' in char_input:
        characters += lowers
    if 'u' in char_input:
        characters += uppers
    if 'n' in char_input:
        characters += numbers
    if 's' in char_input:
        characters += symbols


def create_password():
    password = ''.join(random.choice(characters) for i in range(length))
    return password


def create_passphrase():
    passphrase = r.get_random_word()
    return passphrase


print(create_passphrase())
