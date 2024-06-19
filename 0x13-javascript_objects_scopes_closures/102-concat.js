#!/usr/bin/node
/* concat files */
const result = require('fs');

const first = result.readFileSync(process.argv[2], 'utf8');
const second = result.readFileSync(process.argv[3], 'utf8');

result.writeFileSync(process.argv[4], (first + second));
