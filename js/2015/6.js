import {input} from '../util.js'
import {arraySum} from '../math.js'

const part2 = true

const Xs = Array(1000).fill(null)
const Ys = Array(1000).fill(null)
const grid = Xs.map(x => (Ys.map(y => part2 ? {on:false, bright:0} : false)))

const lightSwitch = (isOn, cmd) => {
    if (cmd === 'turn on') return true
    if (cmd === 'turn off') return false
    if (cmd === 'toggle') return !isOn
}

const brightness = (i, cmd) => {
    if (cmd === 'turn on') return i+1
    if (cmd === 'turn off') return i === 0 ? 0 : i-1
    if (cmd === 'toggle') return i+2
}

const getCoordValues = coord => {
    const [x, y] = coord.split(',')
    return {
        x: Number(x),
        y: Number(y),
    }
}

const parse = i => {
    const [_, cmd, start, end] = i.match(/([\s\w]*) ([\d,]*) through ([\d,]*)/)
    return {
        cmd,
        start: getCoordValues(start),
        end: getCoordValues(end),
    }
}

input.split('\n').forEach(i => {
    const {cmd, start, end} = parse(i)
    for (let x = start.x; x <= end.x; ++x) {
        for (let y = start.y; y <= end.y; ++y) {
            if (!part2) grid[x][y] = lightSwitch(grid[x][y], cmd)
            if (part2) {
                const {on, bright} = grid[x][y]
                grid[x][y] = {
                    on: lightSwitch(on, cmd),
                    bright: brightness(bright, cmd),
                }
            }
        }
    }
})

console.log(
    arraySum(grid.flatMap(row => {
        if (!part2) return row
        if (part2) return row.map(i => i.bright)
    }))
)
