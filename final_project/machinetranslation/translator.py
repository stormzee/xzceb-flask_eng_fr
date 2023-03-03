import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

apikey  = os.environ['APIKEY']
url = os.environ['URL']


translator_auth = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version= '2018-05-01', 
    authenticator=translator_auth
    )

language_translator.set_service_url(url)
language_translator.set_detailed_response(True)


# create functions to translate from eng-frn and vice-versa

def englishToFrench(englishText):
    french_tranlation = language_translator.translate(
        text = englishText,
        source = 'en',
        target = 'fr'
        ).get_result()
    res = json.dumps(
        french_translation,
        indent = 2,
        ensure_ascii = False
        )
    return res


def frenchToEnglish(frenchText):
    eng_tranlation = language_translator.translate(
        text = frenchText,
        source = 'fr',
        target = 'en'
        ).get_result()
    res = json.dumps(
        eng_translation,
        indent = 2,
        ensure_ascii = False
        )
    return res






