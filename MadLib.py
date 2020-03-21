
def MadLib:
    # Should have a text associated with it
    text = None
    # Should have a generated list of required words in the NOUN, ADJECTIVE, VERB format

    def __init__(self):
        # Upon initialization it should generate the list of required words
        # Also during initialization it should replace the action words in self.text with {} so that
            # it can be .formatted()
        self.text = select_random_madlib()

    def select_random_madlib(self):
        # Select a random madlib
    def generateRequiredWords(madlib):
