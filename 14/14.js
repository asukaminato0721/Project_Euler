function main() {
  let sol = new Map();
  let maxi = 0,
    maxcnt = 0;

  for (let i = 1; i <= 1000000; i++) {
    let temp = i;
    let cnt = 1;
    let flag = true;
    while (temp !== 1) {
      if (sol.has(temp)) {
        sol.set(i, cnt + sol.get(temp) - 1);
        flag = false;
        break;
      }
      if (temp % 2 === 0) {
        temp /= 2;
      } else {
        temp = temp * 3 + 1;
      }
      cnt++;
    }
    if (flag) {
      sol.set(i, cnt);
    }
    if (maxcnt < sol.get(i)) {
      maxcnt = sol.get(i);
      maxi = i;
    }
  }
  return maxi;
}
console.assert(main(), 837799);
