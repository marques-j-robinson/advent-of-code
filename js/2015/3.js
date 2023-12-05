import {input} from '../util.js'
const i = input.split('')

const createSanta = () => ({
    x: 0,
    y: 0,
    seen: ['0,0'],
})

const createCoord = ({x, y}) => `${x},${y}`

const move = (santa, direction) => {
    if (direction === '>') santa.x += 1
    if (direction === '<') santa.x -= 1
    if (direction === '^') santa.y += 1
    if (direction === 'v') santa.y -= 1
    const coord = createCoord(santa)
    if (!santa.seen.includes(coord)) {
        santa.seen.push(coord)
    }
}

const removeDups = (arr1, arr2) =>
    ([...arr1,...arr2, ].filter((v, i, self) => i === self.indexOf(v)))

const s = createSanta()
i.forEach(i => move(s, i))
console.log(s.seen.length)

const s1 = createSanta()
const s2 = createSanta()

i.forEach((i, idx) => {
    if (idx%2===0) {
        move(s1, i)
    } else {
        move(s2, i)
    }
})

console.log(removeDups(s1.seen, s2.seen).length)
