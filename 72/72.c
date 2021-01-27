#include <assert.h>
#include <math.h>
#define ll long long
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
ll sol()
{
    ll sum = 0LL;
    for (ll i = 2LL; i < 1000001LL; i++)
        sum += totatives(i);
    return sum;
}
int main()
{
    assert(sol() == 303963552391LL);
    return 0;
}
