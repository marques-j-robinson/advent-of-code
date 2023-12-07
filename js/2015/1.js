import { input } from '../util.js'
import { arraySum } from '../math.js'

const part2 = true

const moveList = input.replaceAll('(', '1,').replaceAll(')', '-1,').split(',').map(i => Number(i))
const isInitBasementEntry = i => i === -1

if (!part2) console.log(arraySum(moveList))

if (part2) {
    let floor = 0
    for (let pos = 0; pos < moveList.length; ++pos) {
        floor += moveList[pos]
        if (isInitBasementEntry(floor)) {
            console.log(pos+1)
            break
        }
    }
}
