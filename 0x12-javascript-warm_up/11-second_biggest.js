#!/usr/bin/node
if (process.argv.length <= 3 || process.argv.length === 3) {
  console.log(0);
} else {
  const nums = process.argv.sort();
  console.log(nums.reverse()[1]);
}
