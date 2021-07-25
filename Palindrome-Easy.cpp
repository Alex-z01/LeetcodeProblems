#include <iostream>

using namespace std;

int count, rev;
bool palin;

bool isPalindrome(int x) {
    int n = x;
    if (x < 0)
    {
        return false;
    }
    while (n != 0)
    {
        int pop = n % 10;
        n /= 10;

        if (rev > INT_MAX / 10 || (rev == INT_MAX / 10 && pop < 7)) { return 0; }
        if (rev < INT_MIN / 10 || (rev == INT_MIN / 10 && pop > -8)) { return 0; }

        rev = rev * 10 + pop;
    }
    if (rev == x)
    {
        palin = true;
    }
    return palin;
}

int main()
{


}