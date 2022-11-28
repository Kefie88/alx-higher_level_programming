#!/usr/bin/node

function fact (n) {
  if (n <= 0) {
    return 0;
  } else if (n === 1) {
    return 1;
  } else {
    return (n * fact(n - 1));
  }
}

const first = parseInt(process.argv[2]);
if (isNaN(first)) {
  console.log('1');
} else {
  console.log(fact(first));
}
