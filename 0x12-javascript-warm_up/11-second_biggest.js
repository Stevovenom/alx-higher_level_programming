#!/usr/bin/node
// The script searches the second biggest integer in the list of arguments.
const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  const sortedArgs = args.sort((a, b) => b - a);
  console.log(sortedArgs[1]);
}
