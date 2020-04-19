from madlib_stories import stories
from Pipeline import Pipeline

import random
import spacy


class MadLib:
    # Take in the class from Pipeline
    # Randomly choose words to change
    # Pass to input class
    word_tag_list = None
    word_locations = None

    def __init__(self, word_tag_list, word_locations):
        self.word_tag_list = word_tag_list
        self.madlib_story = random.choice(stories)
        self.word_requirement_list = self.generate_required_words()
        self.prime_text_for_formatting()
        self.prompt_user_input()
        self.show_complete_madlib()

    def replace_proper_nouns(self, pnoun):
        for index in self.word_locations[pnoun]:
            self.word_tag_list[index][0] = "{}"

    def generate_required_words(self):
        word_list = self.pattern.findall(self.madlib_story)
        return word_list

    def prompt_user_input(self):
        for word in self.word_requirement_list:
            user_word = input("Please enter a {}: ".format(word))
            self.word_list.append(user_word)
