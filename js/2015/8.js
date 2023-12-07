import {input, splitBy} from '../util.js'
import {arraySum} from '../math.js'

const part2 = true

const lines = splitBy(input, '\n')

console.log(
    arraySum(lines.map(s => {
        return part2
            ? JSON.stringify(s).length - s.length
            : s.length - eval(s).length
    }))
)
