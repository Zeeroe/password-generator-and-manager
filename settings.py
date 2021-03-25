characters = {
    'a': 'abcdefghijklmnopqrstuvwxyz',
    'A': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    '1': '0123456789',
    '!': '!@#$%^&*'
}
length = 16

words = 3
minlength = 4
maxlength = 12
sep = '-'
casing = 'title'  # lower, upper, title
number = True


class Settings:
    """ Class for storing generation settings """

    def __init__(self):
        # Password
        self.characters = characters
        self.length = length

        # Passphrase
        self.words = words
        self.minlength = minlength
        self.maxlength = maxlength
        self.sep = sep
        self.casing = casing
        self.number = number


S = Settings()
