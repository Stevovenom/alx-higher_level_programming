#!/usr/bin/node

const dicti = require('./101-data').dict;
const set1 = new Set(Object.values(dicti));

const a = Array.from(set1);

const result = {};
/* fill the dictionary with empty list for each key */
for (let i = 0; i < a.length; i++) {
  result[a[i]] = [];
}
/* fill content of each list */
for (const key1 of Object.keys(result)) {
  for (const key2 of Object.keys(dicti)) {
    if (dicti[key2] === parseInt(key1)) {
      result[key1].push(key2);
    }
  }
}
console.log(result);
