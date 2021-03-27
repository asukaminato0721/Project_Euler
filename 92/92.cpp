#pragma GCC optimize(3, "Ofast", "inline")
#include <bits/stdc++.h>
using namespace std;
#define all(x) x.begin(), x.end()
using ll = long long;
unordered_set<int> solu89 = {89}, solu1 = {1};
int sqrsum(int i)
{
    int s = 0;
    while (i > 0)
    {
        int tmp = i % 10;
        s += tmp * tmp;
        i /= 10;
    }
    return s;
}
void sol(int i)
{
    vector<int> temp = {i};
    while (true)
    {
        if (solu89.count(i))
        {
            solu89.insert(all(temp));
            break;
        }
        else if (solu1.count(i))
        {
            solu1.insert(all(temp));
            break;
        }
        else
        {
            temp.push_back(i);
            i = sqrsum(i);
        }
    }
}
int main()
{
    for (size_t i = 1; i < 10000000; i++)
    {
        sol(i);
    }
    cout << solu89.size();
}
