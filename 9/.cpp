#pragma GCC optimize(3, "Ofast", "inline")
#include <bits/stdc++.h>
using namespace std;
int main()
{
    for (size_t c = 333; c < 1000; c++)
    {
        for (size_t b = 1; b < c; b++)
        {
            for (size_t a = 1; a < b; a++)
            {
                if (a * a + b * b == c * c)
                {
                    cout << a << " " << b << " " << c;
                    return 0;
                }
            }
        }
    }
    return 0;
}
