'''
    This module provides functions to translate
    texts from english to french and vice-versa
    using IBM Watson Language Translator service.
'''

#import json
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


def englishToFrench(englishText):

    '''
        This function translates an english text
        to frech. If the string is None, the
        return value will also be None.
        (Antonio Guglielmi)
    '''

    if englishText is None:
        return None

    translation = language_translator.translate(
                    text=englishText, model_id='en-fr').get_result()

    frenchText = translation['translations'][0]['translation']

    return frenchText



def frenchToEnglish(frenchText):

    '''
        This function translates an english text
        to frech. If the string is None, the
        return value will also be None.
        (Antonio Guglielmi)
    '''

    if frenchText is None:
        return None

    translation = language_translator.translate(
                    text=frenchText, model_id='fr-en').get_result()

    englishText = translation['translations'][0]['translation']

    return englishText
