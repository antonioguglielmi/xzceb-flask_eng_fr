import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    
    def test_e2f_for_null_input(self):
        self.assertIsNone(englishToFrench(None))

    def test_e2f_translation_error(self):
        self.assertNotEqual(englishToFrench('Bye'), 'Bonjour')
    
    def test_e2f_translation(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
    
    def test_f2e_for_null_input(self):
        self.assertIsNone(frenchToEnglish(None))

    def test_f2e_translation_error(self):
        self.assertNotEqual(frenchToEnglish('Au revoir'), 'Hello')

    def test_f2e_translation(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')


if __name__ == '__main__':
    unittest.main(verbosity=2)

