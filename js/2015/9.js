import {input} from '../util.js'
import {permute} from '../array.js'

const part2 = true

const locations = input.split('\n').reduce((acc, i) => {
    const [_, from, to, distance] = i.match(/(\w*) to (\w*) = (\d*)/)
    if (!acc[from]) {
        acc[from] = {}
    }
    acc[from][to] = Number(distance)
    if (!acc[to]) {
        acc[to] = {}
    }
    acc[to][from] = Number(distance)
    return acc
}, {})

const distances = permute(Object.keys(locations)).map(route => {
    let distance = 0
    for (let i = 1; i<route.length; ++i) {
        distance += locations[route[i-1]][route[i]]
    }
    return distance
})

console.log(part2?Math.max(...distances):Math.min(...distances))
