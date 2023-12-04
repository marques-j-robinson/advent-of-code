import {
    input,
    sum,
} from '../util.js'

const p1 = sum(input
    .replaceAll('(', '1,')
    .replaceAll(')', '-1,')
    .split(','))
console.log(p1)
