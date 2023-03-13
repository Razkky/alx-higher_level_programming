#!/usr/bin/node

const size = process.argv.length;
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const nums = [];
  for (let i = 2; i < size; i++) {
    nums[i - 2] = parseInt(process.argv[i]);
  }
  nums.sort();
  nums.reverse();
  console.log(nums[1]);
}
