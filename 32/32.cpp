#pragma GCC optimize(3, "Ofast", "inline")
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
vector<uint32_t> sol;
vector<int> listt(size_t num)
{
    vector<int> a;
    while (num > 0)
    {
        a.push_back(num % 10);
        num /= 10;
    }
    return a;
}
bool iff(const size_t &i, const size_t &j)
{
    vector<int> I = listt(i);
    vector<int> J = listt(j);
    vector<int> IJ = listt(i * j);
    I.insert(I.end(), J.begin(), J.end());
    I.insert(I.end(), IJ.begin(), IJ.end());
    sort(I.begin(), I.end());
    return I == vector<int>{1, 2, 3, 4, 5, 6, 7, 8, 9};
}
int main()
{
    for (size_t i = 1; i < 100; i++)
    {
        for (size_t j = 100; j < 10000; j++)
        {
            if (iff(i, j))
            {
                sol.push_back(i * j);
            }
        }
    }
    sort(sol.begin(), sol.end());
    auto ed = unique(sol.begin(), sol.end());
    ll sum = 0;
    for (auto i = sol.begin(); i != ed; i++)
    {
        sum += *i;
    }
    cout << sum;
    return 0;
}
