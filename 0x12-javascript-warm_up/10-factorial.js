#!/usr/bin/node
const num = parseInt(process.argv[2]);
let ret = 1;
if (isNaN(num) || num === 1) {
    console.log(ret);
} else {
    for (let i = num; i > 0; i--) {
        ret *= i;
    }
    console.log(ret);
}
