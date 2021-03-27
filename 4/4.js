function main() {
  function* t() {
    for (let i = 100; i < 1000; i++) {
      for (let j = i; j < 999; j++) {
        let a = `${i * j}`;
        let b = [...a].reverse().join("");
        if (a === b) {
          yield i * j;
        }
      }
    }
  }
  return Math.max(...t());
}

console.assert(main(), 906609);
