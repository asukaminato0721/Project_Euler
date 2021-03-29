const assert = require("assert").strict;
function main() {
  function* fib() {
    let a = 0,
      b = 1;
    while (a < 400_0000) {
      if (a % 2 === 0) {
        yield a;
      }
      [a, b] = [b, a + b];
    }
  }
  return [...fib()].reduce((a, b) => a + b);
}
assert.equal(main(), 4613732);
