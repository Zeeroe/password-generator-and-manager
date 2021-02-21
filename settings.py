import string

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
casing = 'title'


class Settings:
    def __init__(self):
        self.characters = characters
        self.length = length

        self.separator = separator
        self.limit = limit
        self.minlength = minlength
        self.maxlength = maxlength
        self.casing = casing

    def setcharacters(self):
        # self.characters = my_text.text
        pass

    def setlength(self):
        # self.length = length_textbox.Text
        pass
