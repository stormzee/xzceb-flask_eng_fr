import os
from ibm_watson import LanguageTranslatorV3
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey  = os.environ['APIKEY']
url = os.environ['URL']
translator_auth = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version= '2018-05-01', authenticator=translator_auth)
language_translator.set_service_url(url)
def english_to_french(text):
    '''
    Function to convert english text to french 
    -----------
    Argument:
    text:string
    ------------
    Returns
    english text
    ------------
    '''
    try:
        french_translation = language_translator.translate(text = text,
        source = 'en',
        target = 'fr'
        ).get_result()
        return french_translation
    except ApiException:
        return None
def french_to_english(text):
    '''
    Function to convert french text to english
    -----------
    Argument:
    text:string
    ------------
    Returns
    english text
    ------------
    '''
    try:
        english_translation = language_translator.translate(text = text,
        source = 'fr',
        target = 'en'
        ).get_result()
        return english_translation   
    except ApiException:
        return None
