import {input} from '../puzzle-input.js'
import {sum} from '../array.js'

const parse = i => {
    const [_, direction, steps] = i.match(/([A-Z]) ([0-9]*)/)
    return {direction, steps: Number(steps)}
}

const grid = []
let row = 0
let col = 0

const dig = () => {
    if (!grid[row]) grid[row] = []
    grid[row][col] = '#'
}

// write initial step
dig()

input.split('\n').forEach(i => {
    const {direction, steps} = parse(i)
    let step = 0
    while (step<steps) {
        if (direction === 'U') row = row === 0 ? 0 : row - 1
        if (direction === 'D') ++row
        if (direction === 'L') col = col === 0 ? 0 : col - 1
        if (direction === 'R') ++col
        dig()
        ++step
    }
})

console.log(grid)

console.log(sum(grid.map(row => {
    let min = row.length-1
    let max = 0
    row.forEach((i, idx) => {
        if (i==='#') {
            if (idx<min) min = idx
            if (idx>=max) max = idx+1
        }
    })
    return max-min
})))
