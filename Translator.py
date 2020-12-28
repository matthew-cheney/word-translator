import DictionaryDAO
import Lemmatizer
from domain.DictionaryEntry import DictionaryEntry
from domain.SupportedLanguage import SupportedLanguage


def _LookupInDictionary(lemma: str,
                        language_code: SupportedLanguage) -> DictionaryEntry:
    return DictionaryDAO.getDictionaryEntry(lemma, language_code)


def Translate(word: str, language_code: SupportedLanguage) -> [(str, DictionaryEntry)]:
    """
    Translate single word. Returns empty list if no translation found.
    :param word: 1 words
    :param language_code: language the word string is in
    :return: list of words and phrase with translations
    """
    res = []
    variants = [word, word.lower()]
    for text, lem in Lemmatizer.lemmatize(word, language_code):
        variants.append(lem)
    for text, lem in Lemmatizer.lemmatize(word.lower(), language_code):
        variants.append(lem)
    for lem in variants:
        dbRes = _LookupInDictionary(lem, language_code)
        if dbRes is not None:
            res.append((word, dbRes))
    return res
