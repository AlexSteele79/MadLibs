from madlib_stories import stories
import random
import re


class MadLib:
    pattern = re.compile(r'VERB | ADJECTIVE | NOUN | NAME', re.VERBOSE)

    text = None
    word_list = None

    def __init__(self):
        self.text = random.choice(stories)
        self.word_list = self.generate_required_words()
        self.prime_text_for_formatting()

    def generate_required_words(self):
        word_list = self.pattern.findall(self.text)
        return word_list

    def prime_text_for_formatting(self):
        self.text = re.sub(self.pattern, "{}", self.text)
