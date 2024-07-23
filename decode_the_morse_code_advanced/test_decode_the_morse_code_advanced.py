import unittest

# Importando as funções que serão testadas
from decode_the_morse_code_advanced import decode_bits, decode_morse

class TestMorseCodeDecoding(unittest.TestCase):
    def test_example_from_description(self):
        bits = '1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'
        expected = 'HEY JUDE'
        got = decode_morse(decode_bits(bits))
        self.assertEqual(got, expected, f"Got '{got}', expected '{expected}'")

if __name__ == '__main__':
    unittest.main()
