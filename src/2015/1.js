import {
    input,
    sum,
} from '../util.js'

const p1 = sum(input
    .replaceAll('(', '1,')
    .replaceAll(')', '-1,')
    .split(','))
console.log(p1)

let p2 = 0
let cur = 0

const move = i => i === '(' ? cur += 1 : cur -= 1
const isInitBasementEntry = () => cur === -1

input.split('').forEach((i, position) => {
    move(i)
    if (p2 === 0 && isInitBasementEntry()) {
        p2 = position+1
    }
})
console.log(p2)
