const constants = require("./constants");
const MAX_COUNT = constants.FIZZ_BUZZ_MAX_COUNT;

export function fizzBuzz(number) {
  let value = number;

  if ((number % 3 === 0) && (number % 5 === 0)) {
    value = "FizzBuzz";
  } else if (number % 3 === 0) {
    value = "Fizz";
  } else if (number % 5 === 0) {
    value = "Buzz";
  }

  return value;
}

export function iterate(count) {
  let array = [];
  [...Array(count + 1).keys()].forEach((n) => {
    array.push(fizzBuzz(n));
  });
  array.shift();
  return array;
}

export function execute() {
  iterate(MAX_COUNT).forEach((value) => {
    console.log(value);
  });
}
