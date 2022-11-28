#!/usr/bin/node

let printXtimes = parseInt(process.argv[2]);
if (isNaN(printXtimes) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  while (printXtimes > 0) {
    console.log('C is fun');
    printXtimes--;
  }
}
