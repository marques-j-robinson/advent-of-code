import { input } from '../puzzle-input.js'
import { sum } from '../array.js'

const part2 = true

const replaceDirections = input.replaceAll('(', '1,').replaceAll(')', '-1,')
const directions = replaceDirections.split(',')

if (!part2) console.log(sum(directions))

const isInitBasementEntry = i => i === -1

if (part2) {
    let floor = 0
    for (let pos = 0; pos < directions.length; ++pos) {
        floor += Number(directions[pos])
        if (isInitBasementEntry(floor)) {
            console.log(pos+1)
            break
        }
    }
}
