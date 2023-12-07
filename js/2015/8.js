import {input} from '../util.js'
import {arraySum} from '../math.js'

const part2 = true

const lines = input.split('\n')

console.log(
    arraySum(lines.map(s => {
        return part2
            ? JSON.stringify(s).length - s.length
            : s.length - eval(s).length
    }))
)
