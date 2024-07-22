#include <bits/stdc++.h>

using namespace std;

string duplicate_encoder(const string& word){
	unordered_map<string, bool> hash_table;
	string result = "";

	string word_input = word;
	transform(word_input.begin(), word_input.end(), word_input.begin(), [](unsigned char c){ return tolower(c); });

	for (size_t letter = 0; letter < word_input.length(); letter++)
	{
		if (hash_table.find(word_input.substr(letter, 1)) != hash_table.end()) {
			hash_table[word_input.substr(letter, 1)] = false;
		} else{
			hash_table[word_input.substr(letter, 1)] = true;
		}
	}
	for (size_t letter = 0; letter < word_input.length(); letter++)
	{
		if (hash_table[word_input.substr(letter, 1)]) {
			result += "(";
		} else
			result += ")";
	}

	return result;
}

int main(int argc, char const *argv[])
{
	cout << duplicate_encoder(argv[1]);
	return 0;
}
