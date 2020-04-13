from madlib_stories import stories
<<<<<<< Updated upstream
=======
from Pipeline import Pipeline
from Story import Story

import os
>>>>>>> Stashed changes
import random
import re
import spacy


class MadLib:
<<<<<<< Updated upstream
    pattern = re.compile(r'VERB | ADJECTIVE | NOUN | NAME', re.VERBOSE)

    madlib_story = None
    word_requirement_list = []
    word_list = []
    filled_word_list = []
=======
    madlib_story = Story().corpus
    pipeline = Pipeline(madlib_story)

>>>>>>> Stashed changes

    def __init__(self):
        self.madlib_story = random.choice(stories)
        self.word_requirement_list = self.generate_required_words()
        self.prime_text_for_formatting()
        self.prompt_user_input()
        self.show_complete_madlib()

<<<<<<< Updated upstream
    def generate_required_words(self):
        word_list = self.pattern.findall(self.madlib_story)
        return word_list

=======
>>>>>>> Stashed changes
    def prime_text_for_formatting(self):
        self.madlib_story = re.sub(self.pattern, "%s", self.madlib_story)

    def prompt_user_input(self):
        for word in self.word_requirement_list:
            user_word = input("Please enter a {}: ".format(word))
            self.word_list.append(user_word)

    def show_complete_madlib(self):
        tuple_list = tuple(self.word_list)
<<<<<<< Updated upstream
        print(self.madlib_story % tuple_list)

=======
        # print(self.madlib_story % tuple_list)
>>>>>>> Stashed changes
