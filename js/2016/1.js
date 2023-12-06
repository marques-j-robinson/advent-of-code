import {input} from '../util.js'
import {manhattanDistance} from '../math.js'
const i = input.split(', ').map(i => [i[0], Number(i.slice(1))])
let p2 = 0

const createGrid = () => ({
    x: 0,
    y: 0,
    seen: ['0,0'],
})

const createCoord = ({x, y}) => `${x},${y}`

const move = (g, direction, steps) => {
    let step = 0
    while (step < steps) {
        if (direction === 'E') g.x += 1
        if (direction === 'W') g.x -= 1
        if (direction === 'N') g.y += 1
        if (direction === 'S') g.y -= 1
        const coord = createCoord(g)
        if (p2 === 0 && g.seen.includes(coord)) {
            p2 = manhattanDistance(g.x, g.y)
        }
        if (!g.seen.includes(coord)) {
            g.seen.push(coord)
        }
        ++step
    }
}

const rotate = {
    NR: 'E',
    NL: 'W',
    SR: 'W',
    SL: 'E',
    ER: 'S',
    EL: 'N',
    WR: 'N',
    WL: 'S'
}

const g = createGrid()
let direction = 'N'
i.forEach(([turn, steps]) => {
    direction = rotate[`${direction}${turn}`]
    move(g, direction, steps)
})
console.log(manhattanDistance(g.x, g.y))
console.log(p2)
