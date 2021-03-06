import spacy

class Pipeline:
    nlp = spacy.load('en')
    word_locations = {}
    madlib = None
    tokenized_text = None
    tagged_text = None
    word_tag_list = None

    def __init__(self, madlib):
        self.madlib = madlib
        self.tokenized_text = self.tokenization()
        self.word_tag_list = self.generate_word_tag_list()
        self.replace_proper_nouns("George")
        print(self.word_tag_list)


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

    def replace_proper_nouns(self, pnoun):
        for index in self.word_locations[pnoun]:
            self.word_tag_list[index][0] = "{}"

        def show_tags(self):
            print("Word\tLemma\tTag\tTagW")
            print("____\t_____\t___\t____")
            for token in self.tokenized_text:

                print("{}\t{}\t{}\t{}".format(token.text, token.lemma_,
                token.tag, token.tag_))
