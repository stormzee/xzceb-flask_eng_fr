import os
import sys
import unittest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import translator

class FrenchEnglishTestCase(unittest.TestCase):
    
    def test_null_input(self):
        input_text = ''
        error_message = translator.englishToFrench(input_text)
        self.assertEqual(error_message,
            None
        )
        
    
    def test_hello_to_french(self):
        input_text = 'Hello'
        res = translator.englishToFrench(input_text)
        output_text = res["translations"][0]["translation"]
        self.assertEqual(output_text,"Bonjour")
    

class EnglishFrenchTestCase(unittest.TestCase):
    
    # def test_is_null_input(self):
    #     input_text = ' '
    #     res = translator.frenchToEnglish(input_text)
    #     sentence_length = res["character_count"]
    #     self.assertEqual(sentence_length,0)
    
    def test_bonjour_to_english(self):
        input_text = 'Bonjour'
        res = translator.frenchToEnglish(input_text)
        output_text = res["translations"][0]["translation"]
        self.assertEqual(output_text,"Hello")
        
        

if __name__ == '__main__':
    unittest.main()