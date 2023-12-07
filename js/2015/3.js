import {input, splitBy} from '../util.js'

const part2 = true

const moves = splitBy(input, '')

const createGrid = () => ({
    x: 0,
    y: 0,
    seen: ['0,0'],
})

const createCoord = ({x, y}) => `${x},${y}`

const move = (grid, direction) => {
    if (direction === '>') grid.x += 1
    if (direction === '<') grid.x -= 1
    if (direction === '^') grid.y += 1
    if (direction === 'v') grid.y -= 1
    const coord = createCoord(grid)
    if (!grid.seen.includes(coord)) {
        grid.seen.push(coord)
    }
}

const removeDups = (arr1, arr2) =>
    ([...arr1,...arr2, ].filter((v, i, self) => i === self.indexOf(v)))

if (!part2) {
    const g = createGrid()
    moves.forEach(i => move(g, i))
    console.log(g.seen.length)
}

if (part2) {
    const s1 = createGrid()
    const s2 = createGrid()

    moves.forEach((i, idx) => {
        if (idx%2===0) {
            move(s1, i)
        } else {
            move(s2, i)
        }
    })

    console.log(removeDups(s1.seen, s2.seen).length)
}
