from domain.DictionaryMeaning import DictionaryMeaning


class DictionaryEntry:
    def __init__(self, lemma: str, meanings: [DictionaryMeaning]):
        self.lemma = lemma
        self.meanings = meanings
