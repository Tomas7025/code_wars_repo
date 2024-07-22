def solution(string_input : str):
	result = []
 
 
	while True:
		if string_input.__len__() == 0:
			break		

		temp = string_input[0] + ''
		string_input = string_input[1::]

		if string_input.__len__() == 0:
			temp+='_'
		else:
			temp += string_input[0] + ''
			string_input = string_input[1::]


		result.append(temp)
	
	return result
