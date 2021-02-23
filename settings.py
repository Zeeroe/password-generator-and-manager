lowers = 'abcdefghijklmnopqrstuvwxyz'
uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*'


characters = ''
length = 16

separator = '-'
words = 3
minlength = 4
maxlength = 9
casing = 'title'
number = True


class Settings:
    """ Class for storing generation settings """

    def __init__(self):
        # Password
        self.characters = characters
        self.length = length

        # Passphrase
        self.separator = separator
        self.words = words
        self.minlength = minlength
        self.maxlength = maxlength
        self.casing = casing
        self.number = number
