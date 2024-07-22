import string

def xo(s : str):
	
	number_of_xs = 0
	number_of_os = 0

	for chr in s:
		if chr == 'O' or chr == 'o':
			number_of_os+=1
		elif chr == 'X' or chr == 'x':
			number_of_xs+=1

	if number_of_xs != number_of_os:
		return False
	else:
		return True

if __name__ == '__main__':
	test_cases = [
	   ("ooxx",    True),
	   ("xooxx",   False),
	   ("ooxXm",   True), # Comparison is case-insensitive
	   ("zpzpzpp", True), # when no 'x' and 'o' is present should return true
	   ("zzoo",    False),
	   ("oxOx",    True),
	   ("",        True),  # Empty string contains equal amount of x and o
	]
	
	for t in test_cases:
		if xo(t[0]) != t[1]:
			print(f"Test {t[0]} failed got {xo(t[0])} expected {t[1]}")
		else:
			print(f"Test {t[0]} passed")