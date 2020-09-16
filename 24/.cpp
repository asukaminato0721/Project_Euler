#pragma GCC optimize(3, "Ofast", "inline")
#include <bits/stdc++.h>
using namespace std;
int main()
{
    auto i = vector<int>{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int n = 1000000 - 1;
    for (; n; next_permutation(i.begin(), i.end()), n--)
        ;
    for_each(i.begin(), i.end(), [](const auto &p) { cout << p << " "; });
    return 0;
}
