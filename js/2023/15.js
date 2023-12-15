import {input} from '../util.js'
import {sum} from '../array.js'
const steps = input.split(',')

const hash = str => {
    let total = 0
    str.split('').forEach(s => {
        total += s.charCodeAt(0)
        total = (total*17)%256
    })
    return total
}

console.log(sum(steps.map(hash)))
