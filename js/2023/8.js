import {input} from '../util.js'
import {lcm} from '../math.js'

const part2 = true

const nodes = input.split('\n\n')[1].split('\n').reduce((acc, i) => {
    const [_, key, left, right] = i.match(/([1-9A-Z]*) = \(([1-9A-Z]*), ([1-9A-Z]*)\)/)
    if (!acc[key]) {
        acc[key] = {'R': right, 'L':left}
    }
    return acc
}, {})

const turns = input.split('\n')[0].split('')
const n = turns.length
const getTurnCircular = i => turns[(i%n+n)%n]

const travel = (start, exitHandler) => {
    let node = start
    let step = 0
    while(exitHandler(node)) {
        const turn = getTurnCircular(step)
        node = nodes[node][turn]
        ++step
    }
    return step
}

if (!part2) {
    const start = 'AAA'
    const exitHandler = node => node!=='ZZZ'
    console.log(travel(start, exitHandler))
}

if (part2) {
    const starts = Object.keys(nodes).filter(i => i[i.length-1] === 'A')
    const exitHandler = node => node[node.length-1]!=='Z'
    console.log(
        starts.map(start => travel(start, exitHandler)).reduce(lcm)
    )
}
