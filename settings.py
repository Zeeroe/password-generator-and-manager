lowers = 'abcdefghijklmnopqrstuvwxyz'
uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*'

characters = ''
length = 16

words = 3
sep = '-'
minlength = 4
maxlength = 6
casing = 'lower'
number = True


class Settings:
    """ Class for storing generation settings """

    def __init__(self):
        # Password
        self.characters = characters
        self.length = length

        # Passphrase
        self.words = words
        self.sep = sep
        self.minlength = minlength
        self.maxlength = maxlength
        self.casing = casing
        self.number = number


S = Settings()
