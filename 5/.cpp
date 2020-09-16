#pragma GCC optimize(3, "Ofast", "inline")
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int64_t lcm = 1;
    for (int64_t i = 1; i < 21; i++)
    {
        lcm = lcm * i / __gcd(lcm, i);
    }
    cout << lcm;
    return 0;
}
