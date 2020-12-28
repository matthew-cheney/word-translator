import DictionaryDAO
import Lemmatizer
from domain.DictionaryEntry import DictionaryEntry
from domain.SupportedLanguage import SupportedLanguage


def _LookupInDictionary(lemma: str,
                        language_code: SupportedLanguage) -> DictionaryEntry:
    return DictionaryDAO.getDictionaryEntry(lemma, language_code)


def Translate(word: str, language_code: SupportedLanguage) -> dict:
    """
    Translate single word. Returns empty list if no translation found.
    :param word: 1 words
    :param language_code: language the word string is in
    :return: list of words and phrase with translations
    """
    res = dict()
    variants = dict()
    # variants[word] = [word, word.lower()]
    for w in word.split(' '):
        variants[w] = [w, w.lower()]

    for text in variants.keys():
        lemmas = set()
        for v in variants[text]:
            lemmas.add(v)
        meanings = set()
        for txt, lem in Lemmatizer.lemmatize(text, language_code):
            lemmas.add(lem)
        for lem in lemmas:
            dbRes = _LookupInDictionary(lem, language_code)
            if dbRes is not None:
                meanings.add(dbRes)
        res[text] = meanings

    return res
