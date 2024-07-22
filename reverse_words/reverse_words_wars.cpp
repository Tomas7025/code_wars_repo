#include <bits/stdc++.h>

using namespace std;

string reverse_words(string str)
{
	string temp, result = "";
	istringstream it(str);
	size_t start = 0, pos = 0;	

	while (it >> temp)
	{
		pos = str.find(temp, start);

		if (pos > start) {
			result += str.substr(start, pos - start);
		}

		//cout << temp;
		reverse(temp.begin(), temp.end());
		result += temp;

		start = pos + temp.length();
	}
	

	if (str.length() != start) {
		result += str.substr(start, str.length()-1);
	}
	
	return result;
}

int main(int argc, char const *argv[])
{
	cout << reverse_words("double          spaced  words   ");
	return 0;
}
