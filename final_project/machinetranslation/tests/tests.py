import unittest
import translator

class TestTranslationMethods(unittest.TestCase):
  def test_englishToFrench(self):
    self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')
    self.assertEqual(translator.english_to_french(None), None)
    self.assertNotEqual(translator.english_to_french('Hello'), 'Hello')


  def test_frenchToEnglish(self):
    self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')
    self.assertEqual(translator.french_to_english(None), None)
    self.assertNotEqual(translator.french_to_english('Bonjour'), 'Bonjour')


if __name__ == '__main__':
    unittest.main()

    