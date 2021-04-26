import json
import random
import re
import requests
import tkinter as tk
from random_word import RandomWords

rw = RandomWords()

api_key = [
    "ue07dtenexug3v5duz1zs8ttiy63spay375xn1f32jirc8910",
    "d1468251dcc15bd72245101c1fc07fae5c3747257092d3230",
    "1eirq2gnxpe0x2crebxeo1pdnc3mdk6fpw7io56j6nw02zyj7",
    "c23b746d074135dc9500c0a61300a3cb7647e53ec2b9b658e"
]

class RwPanel:
    def __init__(self, frame, settings):
        self.frame = frame
        self.S = settings

        self.minlength_label = tk.Label(self.frame, text='Keyword')
        self.minlength_label.grid(column=0, row=0)
        self.keyword_entry = tk.Entry(self.frame, width=16, justify=tk.CENTER)
        self.keyword_entry.insert(0, self.S.keyword)
        self.keyword_entry.grid(column=1, row=0)

        self.words_label = tk.Label(self.frame, text='Number of Words')
        self.words_label.grid(column=0, row=1)
        self.words_var = tk.IntVar(value=self.S.words)
        self.words_spinbox = tk.Spinbox(self.frame, from_=1, to=16, width=2, state='readonly',
                                        textvariable=self.words_var, command=self.words_f)
        self.words_spinbox.grid(column=1, row=1)

        self.casing_label = tk.Label(self.frame, text='Casing')
        self.casing_label.grid(column=0, row=3)
        self.casing_list = ['Lowercase', 'Uppercase', 'Titlecase']
        self.casing_var = tk.StringVar(value=self.S.casing)
        self.casing_drop = tk.OptionMenu(self.frame, self.casing_var, *self.casing_list, command=self.casing_f)
        self.casing_drop.grid(column=1, row=3)

        self.reg = self.frame.register(self.separator_f)

        self.sep_label = tk.Label(self.frame, text='Separator')
        self.sep_label.grid(column=0, row=2)
        self.sep_entry = tk.Entry(self.frame, width=2, validate="key", validatecommand=(self.reg, '%P'))
        self.sep_entry.grid(column=1, row=2)
        self.sep_entry.insert(0, self.S.sep)

        self.number_label = tk.Label(self.frame, text='Number')
        self.number_label.grid(column=0, row=4)
        self.number_var = tk.IntVar(self.frame)
        self.number_check = tk.Checkbutton(self.frame, variable=self.number_var, command=self.number_f)
        self.number_check.grid(column=1, row=4)
        self.number_check.invoke()

    def recheck_settings(self):
        self.words_var.set(self.S.words)
        temp = self.S.sep
        self.sep_entry.delete(0, 1)
        self.sep_entry.insert(0, temp)
        self.casing_var.set(self.S.casing)
        self.number_var.set(self.S.number)

    def words_f(self):
        self.S.words = int(self.words_var.get())

    def casing_f(self, c):
        self.S.casing = c

    def separator_f(self, v):
        if len(v) <= 1:
            self.S.sep = v
            return True
        else:
            return False

    def number_f(self):
        if self.number_var.get() == 0:
            self.S.number = False
        elif self.number_var.get() == 1:
            self.S.number = True

    def get_related_words(self, word_id, relation_type, word_limit):
        url = 'https://api.wordnik.com/v4/word.json/' + word_id + '/relatedWords?useCanonical=true&relationshipTypes=' \
              + relation_type + '&limitPerRelationshipType=' + word_limit + ' &api_key=' + api_key[0]
        r = requests.get(url)
        data = json.loads(r.content)
        return data

    def update_text_entry(self, text_entry, text):
        text_entry.delete(0, len(text_entry.get()))
        text_entry.insert(0, text)

    def gen_phrase(self, text_entry):
        word_id = self.keyword_entry.get()
        data = self.get_related_words(word_id, 'synonym', '1000')

        if 'message' in data:  # When Error message is in data
            if data['message'] == 'Not found':
                self.update_text_entry(text_entry, 'No Related Words Found')
            elif data['message'] == 'API rate limit exceeded':
                self.update_text_entry(text_entry, 'API rate limit exceeded')
        else:
            synonyms_list = data[0]['words']
            print(len(synonyms_list), synonyms_list)

            S = self.S
            random.shuffle(synonyms_list)
            list_ = []

            for _ in range(S.words):
                try:
                    word = ''
                    while not re.search(re.compile('^[aA-zZ]{3,}$'), word):  # Word must be 3+ characters and only letters
                        word = synonyms_list.pop()
                    list_.append(word)
                except IndexError:
                    pass

            if S.number:
                index_ = random.randint(0, len(list_) - 1)
                number_ = str(random.randint(0, 9))
                list_[index_] += number_

            passphrase = S.sep.join(list_)

            if S.casing == 'Lowercase':
                passphrase = passphrase.lower()
            elif S.casing == 'Uppercase':
                passphrase = passphrase.upper()
            elif S.casing == 'Titlecase':
                passphrase = passphrase.title()

            text_entry.delete(0, len(text_entry.get()))
            text_entry.insert(0, passphrase)
