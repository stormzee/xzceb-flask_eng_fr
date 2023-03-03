import unittest
from machinetranslation import translator

class FrenchEnglishTestCase(unittest.TestCase):
    
    def test_null_input(self):
        input_text = ''
        res = translator.englishToFrench(input_text)
        sentence_length = res["character_count"]
        self.assertEqual(sentence_length,0)
        
    
    def test_hello_to_french(self):
        input_text = 'Hello'
        res = translator.englishToFrench(input_text)
        output_text = res["translations"][0]["translation"]
        self.assertEqual(output_text,"Bonjour")
    

class EnglishFrenchTestCase(unittest.Testcase):
    
    def test_is_null_input(self):
        input_text = ''
        res = translator.frenchToEnglish(input_text)
        sentence_length = res["character_count"]
        self.assertEqual(sentence_length,0)
    
    def test_bonjour_to_engish(self):
        input_text = 'Bonjour'
        res = translator.englishToFrench(input_text)
        output_text = res["translations"][0]["translation"]
        self.assertEqual(output_text,"Hello")
        
        

if __name__ == '__main__':
    unittest.main()