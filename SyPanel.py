import json
import random
import re
import requests
import tkinter as tk
from random_word import RandomWords

rw = RandomWords()


class SyPanel:
    def __init__(self, frame, settings):
        self.frame = frame
        self.S = settings

        self.minlength_label = tk.Label(self.frame, text='Keyword')
        self.minlength_label.grid(column=0, row=0)
        self.keyword_entry = tk.Entry(self.frame, width=16, justify=tk.CENTER)
        self.keyword_entry.insert(0, 'truth')
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


    def gen_phrase(self, text_entry):
        app_id = 'c423ffa9'
        app_key = '619c968e34e4c06d42aac3bdbe22c5e9'
        language = 'en-gb'
        word_id = self.keyword_entry.get()

        url = 'https://od-api.oxforddictionaries.com/api/v2/entries/' + language + '/' + word_id.lower()
        r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
        data = json.loads(r.content)

        synonyms_list = []

        if 'results' in data:
            senses = data['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
            for sense in senses:
                if 'subsenses' in sense:
                    for subsense in sense['subsenses']:
                        if 'synonyms' in subsense:
                            for synonym in subsense['synonyms']:
                                synonyms_list.append(synonym['text'])
                if 'synonyms' in sense:
                    for synonym in sense['synonyms']:
                        synonyms_list.append(synonym['text'])

        print(len(synonyms_list), synonyms_list)

        if synonyms_list:
            S = self.S
            random.shuffle(synonyms_list)
            list_ = []

            for _ in range(S.words):
                word = synonyms_list.pop()
                while not re.search(re.compile('^[aA-zZ]+$'), word):
                    print(word + ' -> ', end='')
                    word = synonyms_list.pop()
                    print(word)
                list_.append(word)

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

        else:
            text_entry.delete(0, len(text_entry.get()))
            text_entry.insert(0, 'No Synonyms Found')
