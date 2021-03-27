function main() {
  let res = new Set();
  for (let i = 2; i < 101; i++) {
    for (let j = 2; j < 101; j++) {
      res.add(i ** j);
    }
  }
  return res.size;
}
console.assert(main(), 9183);
