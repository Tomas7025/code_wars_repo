def decode_morse(morse_code: str) -> str:
	# Definindo o dicionário MORSE_CODE com os códigos como chaves e letras como valores
	MORSE_CODE = {
		'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
		'..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
		'-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
		'.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
		'..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
		'--..': 'Z',
		'-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
		'.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
		'.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': '\'', '-.-.--': '!',
		'-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
		'-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
		'.-..-.': '"', '...-..-': '$', '.--.-.': '@',
		'...---...': 'SOS'
	}

	# Dividindo a string Morse por palavras
	words = morse_code.strip().split('   ')
	result = []

	# Iterando sobre cada palavra
	for word in words:
		# Dividindo a palavra Morse em caracteres
		chars = word.split(' ')
		# Decodificando cada caractere Morse
		decoded_word = ''.join(MORSE_CODE.get(char, '') for char in chars)
		# Adicionando a palavra decodificada à lista de resultados
		result.append(decoded_word)

	# Juntando todas as palavras decodificadas com espaços entre elas
	return ' '.join(result)

# Teste da função
print(decode_morse('.... . -.--   .--- ..- -.. .'))  # Deve imprimir "HEY JUDE"
print(decode_morse('.-'))  # Deve imprimir "A"
print(decode_morse(' . '))  # Deve imprimir "E"
print(decode_morse('...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-'))  # Deve imprimir "SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."
