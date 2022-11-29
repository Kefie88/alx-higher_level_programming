#!/usr/bin/node

exports.converter = function (base) {
  return function (n) {
    return n.tostring(base)
  }
};	
