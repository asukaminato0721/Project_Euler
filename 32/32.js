const assert = require("assert").strict;

function main() {
  function foo(a, b, c) {
    let array1 = [...new Set(`${a}${b}${c}`)].map((x) => Number(x));
    array1.sort();
    let array2 = [...Array(10).keys()].filter((x) => x > 0);
    return (
      array1.length === array2.length &&
      array1.every((value, index) => value === array2[index])
    );
  }
  function _main() {
    let sum = new Set();
    for (let i = 1; i < 100; i++) {
      for (let j = 100; j < 10000; j++) {
        if (foo(i, j, i * j) && i * j <= 9999) {
          sum.add(i * j);
        }
      }
    }
    return [...sum].reduce((a, b) => a + b);
  }
  return _main();
}
assert.equal(main(), 45228);
