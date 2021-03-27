function main() {
  function foo(a, b, c) {
    let arr = [...new Set(`${a}${b}${c}`)];
    arr.sort();
    return (
      arr.toString() === [...Array(10).keys()].filter((x) => x > 0).toString()
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
console.assert(main(), 45228);
