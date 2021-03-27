function main() {
  let solu89 = new Set([89]);
  let solu1 = new Set([1]);
  function sqrsum(i) {
    let s = 0;
    while (i > 0) {
      let tmp = i % 10;
      s += tmp * tmp;
      i = Math.floor(i / 10);
    }
    return s;
  }
  function sol(i) {
    let temp = [i];
    while (true) {
      if (solu89.has(i)) {
        temp.map((x) => solu89.add(x));
        break;
      } else if (solu1.has(i)) {
        temp.map((x) => solu1.add(x));
        break;
      } else {
        temp.push(i);
        i = sqrsum(i);
      }
    }
  }
  function _main() {
    for (let i = 1; i < 1000_0000; i++) {
      sol(i);
    }
    return solu89.size;
  }
  return _main();
}
console.assert(main(), 8581146);
