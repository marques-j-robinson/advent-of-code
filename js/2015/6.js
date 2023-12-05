import {input, splitByLine} from '../util.js'
const i = splitByLine(input)

const Xs = Array(1000).fill(null)
const Ys = Array(1000).fill(null)
const grid = Xs.map(x => (Ys.map(y => ({on:false, bright:0}))))

export const parseInstruction = i => {
    const [_, cmd, start, end] = i.match(/([\s\w]*) ([\d,]*) through ([\d,]*)/)
    return {cmd, start,end}
}

export const parseCoord = coord => {
    const [x, y] = coord.split(',')
    return {
        x: Number(x),
        y: Number(y),
    }
}

export const handleLightSwitch = (cmd, curVal) => {
    if (cmd === 'turn on') return true
    if (cmd === 'turn off') return false
    if (cmd === 'toggle') return !curVal
}

export const handleBrightness = (cmd, curVal) => {
    if (cmd === 'turn on') return curVal+1
    if (cmd === 'turn off') return curVal === 0 ? 0 : curVal-1
    if (cmd === 'toggle') return curVal+2
}

let p1 = 0
let p2 = 0

i .forEach(i => {
    const {cmd, start, end} = parseInstruction(i)
    const {x:startX, y:startY} = parseCoord(start)
    const {x:endX, y:endY} = parseCoord(end)
    for (let x = startX; x <= endX; ++x) {
        for (let y = startY; y <= endY; ++y) {
            const {on, bright} = grid[x][y]
            grid[x][y] = {
                on: handleLightSwitch(cmd, on),
                bright: handleBrightness(cmd, bright),
            }
        }
    }
})

grid.forEach(row => {
    row.forEach(({on, bright}) => {
        if (on) p1 += 1
        p2 += bright
    })
})
console.log(p1)
console.log(p2)
