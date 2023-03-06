import os
import sys
import unittest
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import translator
class FrenchEnglishTestCase(unittest.TestCase):
    '''Class to test for french to english translator methods in translator module'''
    def test_null_input(self):
        '''Function to test the french to english translation service 
        and handle null entries in requests..
        test name: test_null_input
        Arguments: None'''
        input_text = ''
        error_message = translator.french_to_english(input_text)
        self.assertEqual(error_message, None)
    def test_french_to_english(self):
        '''Function to test the french to english translation service,
        converts french 'bonjour' to english 'Hello'
        test name: test_french_to_english
        Arguments: None
        Returns:
        True assert statement'''
        input_text = 'Bonjour'
        res = translator.french_to_english(input_text)
        output_text = res["translations"][0]["translation"]
        self.assertEqual(output_text,"Hello")
    def test_not_bonjour_to_english(self):
        '''Function to test false assert statements for the french to english s
        ervice/function
        Arguments: None
        Returns:
        Not Equal assert statement'''
        input_text = 'Bonjour'
        res = translator.french_to_english(input_text)
        output_text = res["translations"][0]["translation"]
        self.assertNotEqual(output_text,"My Bag")   
class EnglishFrenchTestCase(unittest.TestCase):
    '''Class to test for english to french translator methods in translator module'''
    def test_is_null_input(self):
        '''Function to test the french to english translation service,
        converts french 'bonjour' to english 'Hello'
        test name: test_french_to_english
        Arguments: None
        Returns:
        True assert statement'''
        input_text = ''
        error_message = translator.english_to_french(input_text)
        self.assertEqual(error_message, None)
    def test_not_hello_to_french(self):
        '''Function to test for incorrect french translations'''
        input_text = 'Hello'
        res = translator.english_to_french(input_text)
        output_text = res["translations"][0]["translation"]
        self.assertNotEqual(output_text,"S'appelle")         
    def test_english_to_french(self):
        '''Function to test english to french
        test name: test_english_to_french
        Returns:
        Assert true statements'''
        input_text = 'Hello'
        res = translator.english_to_french(input_text)
        output_text = res["translations"][0]["translation"]
        self.assertEqual(output_text,"Bonjour")
if __name__ == '__main__':
    unittest.main()
