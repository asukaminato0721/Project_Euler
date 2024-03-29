const assert = require("assert").strict;
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
  return [...Array(1000000 + 1).keys()]
    .filter((x) => x >= 2)
    .map(totatives)
    .reduce((a, b) => a + b);
}
assert.equal(main(), 303963552391);
