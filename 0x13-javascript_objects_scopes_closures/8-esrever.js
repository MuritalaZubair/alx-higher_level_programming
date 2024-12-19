#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight((array, current) => {
    array.push(current);
    return array;
  }, []);
};
