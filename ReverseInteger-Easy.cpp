#include <iostream>
#include <string>

using namespace std;

long int revNum = 0;
string num, newNum;
bool negative;

int reverse(int x) {
	
	if (x < 2147483647 && x > -2147483647) {
		num = to_string(x);
		if (x < 0)
		{
			negative = true;
		}

		for (int i = num.length(); i > 0; i--)
		{
			newNum += num[i - 1];
		}

		revNum = stol(newNum);

		if (negative) {
			revNum /= -1;
		}
	}
	else {
		revNum = 0;
	}
	return revNum;
}

int main() {
	cout << reverse(1534236469) << endl;
}