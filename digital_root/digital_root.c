#include <stdio.h>

int __number_size(int number) {
	int size = 1;
	number = number < 0 ? -number : number;

	while (number >= 10)
	{
		number/=10;
		size++;
	}
	
	return size;
}

int digital_root(int n) {

	int total, temp;

	if (__number_size(n) == 1)
		return n;

	while ((temp = __number_size(n)) != 1)
	{
		int base10 = 1;
		total = 0;
		for (int _ = 0; _ < temp; _++, base10*=10)
		{
			total+= (n/base10)%10;
		}

		n = total;		
	}
	
	return total;
}
