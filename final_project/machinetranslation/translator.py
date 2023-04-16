"""This module translate En-Fr and Fr-En"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def translate_english_to_french(text):
    """
    This method translate En-Fr
    """
    translation = language_translator.translate(
        text=text,
        source='en',
        target='fr'
    ).get_result()
    translated_text = translation['translations'][0]['translation']
    return translated_text

def translate_french_to_english(text):
    """
This method translate Fr-En
"""
    translation = language_translator.translate(
        text=text,
        source='fr',
        target='en'
    ).get_result()
    translated_text = translation['translations'][0]['translation']
    return translated_text
