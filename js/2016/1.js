import {input} from '../util.js'
import {manhattanDistance} from '../math.js'
const i = input.split(', ').map(i => [i[0], Number(i.slice(1))])

const createGrid = () => ({
    x: 0,
    y: 0,
    seen: ['0,0'],
})

const createCoord = ({x, y}) => `${x},${y}`

const move = (grid, direction, steps) => {
    if (direction === 'E') grid.x += steps
    if (direction === 'W') grid.x -= steps
    if (direction === 'N') grid.y += steps
    if (direction === 'S') grid.y -= steps
    const coord = createCoord(grid)
    if (!grid.seen.includes(coord)) {
        grid.seen.push(coord)
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
