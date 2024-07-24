import itertools
import numpy as np

def golomb(input_sequence, output_len):
	result = np.full(output_len, -1)
	
	if hasattr(input_sequence, 'fn'):
		input_sequence_array = list(itertools.islice(input_sequence, output_len))
	else:
		input_sequence_array = input_sequence
	
	print(input_sequence_array)
	
	pointer = 0
	
	if input_sequence_array[0] != 0:
		for term in range(len(input_sequence_array)):
			if pointer == output_len:
				break
			elif result[term] == -1:
				for i in range(input_sequence_array[term]):
					result[pointer] = input_sequence_array[term]
					pointer += 1
					if pointer == output_len:
						break
			else:
				for i in range(result[term]):
					result[pointer] = input_sequence_array[term]
					pointer += 1
					if pointer == output_len:
						break
	else:
		if input_sequence_array[1] == 1:
			result[0] = 1
			result[1] = input_sequence_array[2]
			result[2] = 1
			result[3] = 0

			pointer = 4
			for i in range(input_sequence_array[2]-2):
				result[pointer] = 1
				pointer+=1
				if pointer == output_len:
					return result.tolist()
			
			for term in range(4, len(input_sequence_array)):
				if pointer == output_len:
					break
				elif result[term] == -1:
					for i in range(input_sequence_array[term]):
						result[pointer] = input_sequence_array[term]
						pointer += 1
						if pointer == output_len:
							break
				else:
					for i in range(result[term]):
						result[pointer] = input_sequence_array[term]
						pointer += 1
						if pointer == output_len:
							break
		else:
			result[0] = input_sequence_array[1]
			result[1] = input_sequence_array[1]
			pointer = 2
   
			for i in range(input_sequence_array[1]):
				result[pointer] = 0
				pointer+=1
				if pointer == output_len:
							break
			
			temp = pointer
			
			for i in range(input_sequence_array[1]-2):
				result[pointer] = input_sequence_array[1]
				pointer+=1
				if pointer == output_len:
							break
   
			for term in range(temp, len(input_sequence_array)):
				if pointer == output_len:
					break
				elif result[term] == -1:
					for i in range(input_sequence_array[term]):
						result[pointer] = input_sequence_array[term]
						pointer += 1
						if pointer == output_len:
							break
				else:
					for i in range(result[term]):
						result[pointer] = input_sequence_array[term]
						pointer += 1
						if pointer == output_len:
							break
			
			
	return result.tolist()

#main
if __name__ == "__main__":
	input_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	input_sequence2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
	input_sequence3 = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
	output_len = 25
	print(input_sequence3)
	result = golomb(input_sequence3, output_len)
	print(result)
