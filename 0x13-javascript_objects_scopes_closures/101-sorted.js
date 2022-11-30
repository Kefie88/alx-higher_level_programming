#!/usr/bin/node

const {dict} = require('./101-data');
const newDict = {};
for (const N in dict) {
  if (newDict[dict[N]] === undefined) {
    newDict[dict[N]] = [];
  }
  newDict[dict[N]].push(N);
}
console.log(newDict);
