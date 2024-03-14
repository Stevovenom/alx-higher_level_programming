#!/usr/bin/node
// the use of parseInt for conversion
const var1 = process.argv[2];
const var2 = parseInt(var1);

if (!isNaN(var2)) {
  console.log('My number:', var2);
} else {
  console.log('Not a number');
}
