import unittest
from translator import translate_english_to_french
from translator import translate_french_to_english

class TestTranslation(unittest.TestCase):

    def test_english_to_french(self):
        # Test a simple English phrase
        english_text = 'Hello, world!'
        expected_french_text = 'Bonjour, le monde !'
        actual_french_text = translate_english_to_french(english_text)
        self.assertEqual(actual_french_text, expected_french_text)

    def test_NotEqualenglish_to_french(self):
        # Test a simple English phrase
        english_text = 'Hello!'
        expected_french_text = 'Bonjour, le monde !'
        actual_french_text = translate_english_to_french(english_text)
        self.assertNotEqual(actual_french_text, expected_french_text)

    def test_french_to_english(self):
        # Test a simple English phrase
        french_text = 'Bonjour le monde !'
        expected_english_text = 'Hello world!'
        actual_english_text = translate_french_to_english(french_text)
        self.assertEqual(actual_english_text, expected_english_text)
    def test_NotEqual_french_to_english(self):
        # Test a simple English phrase
        french_text = 'Bonjour le monde !'
        expected_english_text = 'Hello'
        actual_english_text = translate_french_to_english(french_text)
        self.assertNotEqual(actual_english_text, expected_english_text)






if __name__ == '__main__':
    unittest.main()