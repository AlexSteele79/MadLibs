
def MadLib:
    # Should have a text associated with it
    text = None
    # Should have a generated list of required words in the NOUN, ADJECTIVE, VERB format
    word_list = None

    def __init__(self):
        # Upon initialization it should generate the list of required words
        # Also during initialization it should replace the action words in self.text with {} so that
            # it can be .formatted()
        self.text = select_random_madlib()
        self.word_list = generate_required_words(self.text)
        self.text = prime_text_for_formatting(self.text)

    def select_random_madlib(self):
        # Select a random madlib

    def generate_required_words(madlib):
        # Generates and returns the required word list

    def prime_text_for_formatting(unformatted_madlib):
        # Remove all required word types and replace with {}