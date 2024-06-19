#!/usr/bin/node
/* creating a function */
exports.esrever = function (list) {
  const size = list.length;
  const result = [];
  for (let i = size - 1; i >= 0; i--) {
    result.push(list[i]);
  }
  return (result);
};
