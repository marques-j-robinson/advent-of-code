import { input, splitBy } from '../util.js'
import { arraySum } from '../math.js'

const part2 = true

const replaceDirections = input.replaceAll('(', '1,').replaceAll(')', '-1,')
const directions = splitBy(replaceDirections, ',')

if (!part2) console.log(arraySum(directions))

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
