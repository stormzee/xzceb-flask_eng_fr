import json
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
import sys
from dotenv import load_dotenv

load_dotenv()

apikey  = os.environ['APIKEY']
url = os.environ['URL']


translator_auth = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version= '2018-05-01', 
    authenticator=translator_auth
    )

language_translator.set_service_url(url)
# language_translator.set_detailed_response(True)


# create functions to translate from eng-frn and vice-versa

def englishToFrench(englishText):
    try:
        french_translation = language_translator.translate(
        text = englishText,
        source = 'en',
        target = 'fr'
        ).get_result()
        return french_translation
    except ApiException as error:
        if str(error.message) == "400":
            return "text is empty"
        else:
            error.message
    


def frenchToEnglish(frenchText):
    try:
        english_translation = language_translator.translate(
            text = frenchText,
            source = 'fr',
            target = 'en'
            ).get_result()
        return english_translation
    except ApiException as error:
        return error.message





