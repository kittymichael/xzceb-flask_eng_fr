"""translate test """
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """class docstring"""
    def test_null_input_returns_error_message(self):
        """
        "Prueba si la función english_to_french devuelve un 
        mensaje de error cuando se proporciona un valor nulo como entrada
        """
        self.assertEqual(english_to_french(None), 'ValueError: text must be provided')

    def test_hello_translates_to_bonjour(self):
        """
        Test that the English word 'Hello' translates to the French word 'Bonjour'.
        """
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_hello_does_not_translate_to_hi_there(self):
        """
        Test that the English word 'Hello' translates to the French word 'Bonjour'.
        """
        self.assertNotEqual(english_to_french('Hello'), 'Hi There')

class TestFrenchToEnglish(unittest.TestCase):
    """class docstring"""
    def test_null_input_returns_error_message(self):
        """Test that the English word 'Hello' translates to the French word 'Bonjour'.

        """
        self.assertEqual(french_to_english(None), 'ValueError: text must be provided')

    def test_bonjour_translates_to_hello(self):
        """Test that the English word 'Hello' translates to the French word 'Bonjour'.

        """
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_bonjour_does_not_translate_to_bonne_journee(self):
        """Test that the English word 'Hello' translates to the French word 'Bonjour'.

        """
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonne Journee')

if __name__ == '__main__':
    unittest.main()
