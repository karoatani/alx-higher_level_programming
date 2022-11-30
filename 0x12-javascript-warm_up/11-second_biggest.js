#!/usr/bin/node

function second(myArray) {

  let num = myArray[0];
  let secondMax = myArray[1];

  for (let i = 0; i < myArray.length; i++) {
    if (myArray[i] > num) {
      secondMax = num;
      num = myArray[i];
    }
  }
  return (secondMax);
}

console.log(second(process.argv));
