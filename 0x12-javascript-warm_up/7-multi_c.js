#!/usr/bin/node
// The script prints x times 'c is fun'
const times = parseInt(process.argv[2]);
if (!isNaN(times) && times > 0) {
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
