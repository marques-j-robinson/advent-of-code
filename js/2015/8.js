import {input, splitByLine} from '../util.js'
import {arraySum} from '../math.js'
const i = splitByLine(input)

console.log(arraySum(i.map(s => s.length - eval(s).length)))
console.log(arraySum(i.map(s => JSON.stringify(s).length - s.length)))
