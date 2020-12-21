from domain.DictionaryEntry import DictionaryEntry
from domain.DictionaryMeaning import DictionaryMeaning
from domain.SupportedLanguage import SupportedLanguage


def getDictionaryEntry(lemma: str, language_code: SupportedLanguage) -> DictionaryEntry:
    return DictionaryEntry(lemma, [DictionaryMeaning("taco", "{n}", "a tasty Mexican food")])