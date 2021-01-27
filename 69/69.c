#include <assert.h>
#include <math.h>
#define ll long long
#define max(x, y, key) (key(x) > key(y) ? x : y)
ll totatives(ll n)
{
    ll phi = n;
    for (ll p = 2LL; p < sqrt(n) + 1; p++)
        if (n % p == 0)
        {
            phi -= phi / p;
            while (n % p == 0)
                n /= p;
        }
    //if n is > 1 it means it is prime
    if (n > 1)
        phi -= phi / n;
    return phi;
}
long double key(ll n)
{
    return (long double)n / totatives(n);
}
int main()
{
    int Max = 0;
    for (int i = 3; i < 1000001; i++)
    {
        Max = max(Max, i, key);
    }
    assert(Max == 510510);
}