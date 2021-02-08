import random
import string
from random_word import RandomWords
rw = RandomWords()

lowers = string.ascii_lowercase
uppers = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

characters = lowers+uppers+numbers
length = 16
separator = '-'
limit = 3
minlength = 4
maxlength = 12
casing = '.title()'


class Settings:
    def __init__(self):
        self.characters = characters
        self.length = length
        
        self.separator = separator
        self.limit = limit
        self.minlength = minlength
        self.maxlength = maxlength
        self.casing = casing


DS = Settings()  # Default Settings


def create_password():
    try:
        password = ''.join(random.choice(DS.characters) for _ in range(DS.length))
        return password
    except Exception:
        pass


def create_passphrase():
    try:
        passphrase = DS.separator.join(rw.get_random_words(limit=DS.limit, minLength=DS.minlength, maxLength=DS.maxlength))

        if DS.casing == 'title':
            passphrase = passphrase.title()

        return passphrase

    except Exception:
        pass


print(create_password())
print(create_passphrase())
