#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nbOc = 0;
  list.forEach(element => {
    if (element === searchElement) nbOc++;
    return nbOc;
  });
};
