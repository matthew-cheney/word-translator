import DictionaryDAO
import Lemmatizer
from domain.DictionaryEntry import DictionaryEntry
from domain.SupportedLanguage import SupportedLanguage


def _LookupInDictionary(lemma: str,
                        language_code: SupportedLanguage) -> DictionaryEntry:
    return DictionaryDAO.getDictionaryEntry(lemma, language_code)


def Translate(words: str, language_code: SupportedLanguage) -> [(str, DictionaryEntry)]:
    """
    Translate both whole words string and tokenized string. Returns empty list if no translation found.
    :param words: 1 or more words
    :param language_code: language the word string is in
    :return: list of words and phrase with translations
    """
    res = []
    wholePhrase = _LookupInDictionary(words, language_code)
    if wholePhrase is not None:
        res.append(wholePhrase)
    for text, lem in Lemmatizer.lemmatize(words, language_code):
        res.append((text, _LookupInDictionary(lem, language_code)))
    return res
