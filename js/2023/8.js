import {input} from '../util.js'

const turns = input.split('\n')[0].split('')
const n = turns.length
const nodes = input.split('\n\n')[1].split('\n').reduce((acc, i) => {
    const [_, key, left, right] = i.match(/([A-Z]*) = \(([A-Z]*), ([A-Z]*)\)/)
    if (!acc[key]) {
        acc[key] = {'R': right, 'L':left}
    }
    return acc
}, {})

let cur = 'AAA'
let step = 0
while (cur !== 'ZZZ') {
    const turn = turns[(step%n+n)%n]
    cur = nodes[cur][turn]
    ++step
}
console.log(step)
