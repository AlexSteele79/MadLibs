from madlib_stories import stories
import random
import re

class MadLib:
    # Should have a text associated with it
    text = None
    # Should have a generated list of required words in the NOUN, ADJECTIVE, VERB format
    word_list = None

    def __init__(self):
        # Also during initialization it should replace the action words in self.text with {} so that
            # it can be .formatted()
        self.text = random.choice(stories)
        # self.word_list = generate_required_words(self.text)
        self.word_list = generate_required_words()
        # self.text = prime_text_for_formatting(self.text)

    def generate_required_words(self):
        search_pattern = re.compile(r'VERB | ADJECTIVE | NOUN | NAME', re.VERBOSE)
        word_list = search_pattern.findall(self.text)

        return word_list

    def prime_text_for_formatting(unformatted_madlib):
        # Remove all required word types and replace with {}


newLib = MadLib()
print(newLib.word_list)