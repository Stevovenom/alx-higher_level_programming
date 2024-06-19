#!/usr/bin/node
/* import a list */
const lista = require('./100-data').list;

const mapeado = lista.map((x, index) => {
  return x * index;
});
console.log(lista);
console.log(mapeado);
