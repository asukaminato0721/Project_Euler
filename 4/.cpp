#pragma GCC optimize(3, "Ofast", "inline")
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int maxm = 0;
    for (size_t i = 100; i < 1e4; i++)
    {
        for (size_t j = i; j < 1e3; j++)
        {
            auto ij = to_string(i * j);
            auto ji = ij;
            reverse(ji.begin(), ji.end());
            if (stoi(ij) == stoi(ji))
            {
                maxm = max(stoi(ij), maxm);
            }
        }
    }
    cout << maxm;
    return 0;
}
