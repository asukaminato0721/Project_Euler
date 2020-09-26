#pragma GCC optimize(3, "Ofast", "inline")
#include <bits/stdc++.h>
using namespace std;
map<size_t, int> sol;
using T = const decltype(sol)::value_type &;
int main()
{
    for (size_t p = 3; p < 1001; p++)
    {
        for (size_t c = p / 2; c < p; c++)
        {
            for (size_t b = 1; b < c; b++)
            {
                if ((p - b - c) * (p - b - c) + b * b == c * c && (p - b - c) > 0)
                {
                    sol[p]++;
                }
            }
        }
    }
    cout << max_element((sol).begin(), (sol).end(), [](T p1, T p2) { return p2.second > p1.second; })->first;
    return 0;
}
