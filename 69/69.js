function main() {
  function totatives(n) {
    let phi = n;
    for (let p = 2; p < Math.sqrt(n) + 1; p++)
      if (n % p === 0) {
        phi -= phi / p;
        while (n % p === 0) n /= p;
      }
    //if n is > 1 it means it is prime
    if (n > 1) phi -= phi / n;
    return phi;
  }
  function key(n) {
    return n / totatives(n);
  }
  return [...Array(1000000).keys()]
    .filter((x) => x >= 3)
    .reduce((a, b) => (key(a) > key(b) ? a : b));
}
console.assert(main(), 510510);
