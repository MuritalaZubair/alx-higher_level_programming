#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size) || size <= 0) {
  console.log('Missing size');
} else {
  for (let r = 0; r < size; r++) {
    console.log('X'.repeat(size));
  }
}
