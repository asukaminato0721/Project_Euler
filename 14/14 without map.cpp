#pragma GCC optimize(3, "Ofast", "inline")
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
ll sol[1000001] = {0};
ll maxi = 0, maxcnt = 0;
int main()
{
    for (size_t i = 1; i <= 1000000; i++)
    {
        auto temp = i;
        int cnt = 1;
        bool flag = true;
        while (temp != 1)
        {
            if (sol[i])
            {
                sol[i] = cnt + sol[temp] - 1;
                flag = false;
                break;
            }
            if (temp % 2 == 0)
            {
                temp /= 2;
            }
            else
            {
                temp = temp * 3 + 1;
            }
            cnt++;
        }
        if (flag)
        {
            sol[i] = cnt;
        }
        if (maxcnt < sol[i])
        {
            maxcnt = sol[i];
            maxi = i;
        }
    }
    cout << maxi;
    return 0;
}
