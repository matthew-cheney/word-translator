import DictionaryDAO
import Lemmatizer
from domain.DictionaryEntry import DictionaryEntry
from domain.SupportedLanguage import SupportedLanguage


def _LookupInDictionary(lemma: str,
                        language_code: SupportedLanguage) -> DictionaryEntry:
    return DictionaryDAO.getDictionaryEntry(lemma, language_code)


def Translate(words: str, language_code: SupportedLanguage) -> [(str, DictionaryEntry)]:
    res = []
    for text, lem in Lemmatizer.lemmatize(words, language_code):
        res.append((text, _LookupInDictionary(lem, language_code)))
    # TEMPORARY FIX - ONLY SUPPORTS SINGLE WORDS
    if len(res) == 0:
        return [_LookupInDictionary(words, language_code)]
    return res
