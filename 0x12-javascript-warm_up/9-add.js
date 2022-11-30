#!/usr/bin/node
function add(a, b) {
  if (process.argv.length == 4 && !isNaN(parseInt(process.argv[2])) && !isNaN(parseInt(process.argv[3]))) {
    console.log(parseInt(a) + parseInt(b));
  }
}
add(process.argv[2], process.argv[3]);
