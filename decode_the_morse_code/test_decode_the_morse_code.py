import unittest

try:
	from decode_the_morse_code import decodeMorse as decode_morse
except ImportError:
	from decode_the_morse_code import decode_morse

class TestMorseCode(unittest.TestCase):
	
	def test_morse_hey_jude(self):
		self.assertEqual(decode_morse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')
	
	def test_morse_basic_examples(self):
		self.assertEqual(decode_morse('.-'), 'A')
		self.assertEqual(decode_morse('--...'), '7')
		self.assertEqual(decode_morse('...-..-'), '$')
		self.assertEqual(decode_morse('.'), 'E')
		self.assertEqual(decode_morse('..'), 'I')
		self.assertEqual(decode_morse('. .'), 'EE')
		self.assertEqual(decode_morse('.   .'), 'E E')
		self.assertEqual(decode_morse('...-..- ...-..- ...-..-'), '$$$')
		self.assertEqual(decode_morse('----- .---- ..--- ---.. ----.'), '01289')
		self.assertEqual(decode_morse('.-... ---...   -..-. --...'), '&: /7')
		self.assertEqual(decode_morse('...---...'), 'SOS')
		self.assertEqual(decode_morse('... --- ...'), 'SOS')
		self.assertEqual(decode_morse('...   ---   ...'), 'S O S')
	
	def test_morse_basic_examples_with_extra_spaces(self):
		self.assertEqual(decode_morse(' . '), 'E')
		self.assertEqual(decode_morse('   .   . '), 'E E')
	
	def test_morse_complex_example(self):
		self.assertEqual(decode_morse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '), 'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')

if __name__ == '__main__':
	unittest.main()
