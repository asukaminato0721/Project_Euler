#pragma GCC optimize(3, "Ofast", "inline")
#include <bits/stdc++.h>
using namespace std;
#define all(x) x.begin(), x.end()
set<int64_t> a, b, c, d;
vector<int64_t> tmp;
int main()
{
    for (int64_t i = 1; i < 100000; i++)
    {
        a.insert(i * (i + 1ll) / 2ll);
        b.insert(i * (3ll * i - 1ll) / 2ll);
        c.insert(i * (2ll * i - 1ll));
    }
    set_intersection(all(a), all(b), back_inserter(tmp));
    d = set<int64_t>(all(tmp));
    tmp.clear();
    set_intersection(all(c), all(d), back_inserter(tmp));
    for (auto &&i : tmp)
    {
        printf("%lld  ", i);
    }
    return 0;
}
