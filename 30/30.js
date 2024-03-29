const assert = require("assert").strict;

function main() {
  function iff(n) {
    return (
      n > 1 &&
      n === [...String(n)].map((x) => Number(x) ** 5).reduce((a, b) => a + b)
    );
  }
  return [...Array(1000000).keys()].filter(iff).reduce((a, b) => a + b);
}
assert.equal(main(), 443839);
