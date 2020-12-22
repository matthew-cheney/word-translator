from bson import ObjectId

from Utils import generateKey
from config import config
from domain.DictionaryEntry import DictionaryEntry
from domain.DictionaryMeaning import DictionaryMeaning
from domain.SupportedLanguage import SupportedLanguage
import json
from pymongo import MongoClient


def _readFromDatabase(key: str, client: MongoClient) -> dict:
    return client[config['db_name']].db.translations.find_one({'_id': key})


def _writeToDatabase(key: str, value: str, client: MongoClient):
    client[config['db_name']].db.translations.insert_one({'_id': key, 'meanings': value})


def getDictionaryEntry(lemma: str, language_code: SupportedLanguage) -> DictionaryEntry:
    # with open(f'JsonDictionaries/{language_code}-en-dictionary.json') as f:
    #     dictionary = json.load(f)
    client = MongoClient()
    res = DictionaryEntry(lemma, [])
    for ea in _readFromDatabase(generateKey(lemma, language_code), client):
        res.meanings.append(DictionaryMeaning(ea['lemma'], ea['pos'], ea['meaning']))
    return res

_writeToDatabase('es_hablar', json.dumps([DictionaryMeaning('talk', '{v}', 'to speak').__dict__]), MongoClient())