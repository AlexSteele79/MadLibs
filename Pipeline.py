import spacy


class Pipeline:
    nlp = spacy.load('en')

    madlib = None
    tokenized_text = None
    word_tag_list = None
    word_locations = {}

    def __init__(self, madlib):
        self.madlib = madlib
        self.tokenized_text = self.tokenization()
        self.word_tag_list = self.generate_word_tag_list()

    def tokenization(self):
        return self.nlp(self.madlib)

    # Creates the object [ [Word, Tag, Tag_], [Word, Tag, Tag_] ]
    def generate_word_tag_list(self):
        return_list = []
        index = 0

        for token in self.tokenized_text:
            text = token.text
            tag = token.tag
            tag_ = token.tag_

            return_list.append([text, tag, tag_])

            try:
                self.word_locations[text].append(index)
            except Exception as e:
                self.word_locations[text] = [index]

            index += 1

        return return_list


if __name__ == "__main__":
    newt = Pipeline("George was a happy King. George was also the only King.")