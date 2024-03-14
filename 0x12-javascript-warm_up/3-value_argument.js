#!/usr/bin/node
// prints the first argument passed to it
const [,, arg] = process.argv;

if (!arg)
{
	console.log('No argument');
}
else
{
	console.log(arg);
}

