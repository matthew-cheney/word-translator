from domain.DictionaryEntry import DictionaryEntry
from domain.DictionaryMeaning import DictionaryMeaning
from domain.SupportedLanguage import SupportedLanguage
import json


def getDictionaryEntry(lemma: str, language_code: SupportedLanguage) -> DictionaryEntry:
    with open(f'JsonDictionaries/{language_code}-en-dictionary.json') as f:
        dictionary = json.load(f)
    res = DictionaryEntry(lemma, [])
    if lemma not in dictionary:
        return None
    for ea in dictionary[lemma]:
        res.meanings.append(DictionaryMeaning(ea['lemma'], ea['pos'], ea['meaning']))
    return res

print(getDictionaryEntry('hablar', SupportedLanguage.es))