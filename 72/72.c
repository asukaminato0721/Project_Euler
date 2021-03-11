// gcc -shared  -s -O2 -DNDEBUG 69.c -o 69.dll
#include <math.h>
int totatives(int n)
{
    int phi = n;
    for (int p = 2; p < sqrt(n) + 1; p++)
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