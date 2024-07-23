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

def decode_bits(bits : str) -> str:
	transmision_rate = 0
	
	bits = bits.strip('0')

	# Primeiro, crie uma lista única com os elementos divididos por '0'
	unique = list(set(bits.split('0')))

	# Em seguida, adicione os elementos únicos divididos por '1' à lista existente
	unique.extend(list(set(bits.split('1'))))

	# Agora, remova quaisquer strings vazias da lista
	while '' in unique:
		unique.remove('')
		
	transmision_rate = min([len(i) for i in unique])

	p_between_words = '0' * transmision_rate * 7
	p_between_letters = '0' * transmision_rate * 3
	p_between_symbols = '0' * transmision_rate

	words = bits.split(p_between_words)
	result_morse = ''
 
	print(f"Transmition rate: {transmision_rate}\nDelay between words: {p_between_words}\nDelay between chars: {p_between_letters}\nDelay between symbols: {p_between_symbols}\n")
	print(f"Word list:\n{words}\n")
	for w in words:
		chars = w.split(p_between_letters)
		temp = ''
		print(f"Character list:\n{chars}\n")
		for c in chars:
			symbols = c.split(p_between_symbols)
			sym = ''
			print(f"Symbol list of char:\n{symbols}\n")
			for s in symbols:
				if s == '1' * transmision_rate * 3:
					sym+='-'
				else:
					sym+='.'
			temp+=sym+' '
		result_morse += temp+'  '
	
	result_morse = result_morse.strip(' ')
	print(f"Morse code sequence:\n==>>>{result_morse}<<<==")
	return result_morse


if __name__ == '__main__':
	print("->>>"+decode_morse(decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')))
