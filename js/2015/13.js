import {input} from '../puzzle-input.js'
import {permute} from '../array.js'

const table = {}

const regex = /([a-zA-Z]*) would ([gain|lose]*) ([0-9]*) [a-z ]* to ([a-zA-Z]*)./
function parse(instruction) {
    const [_, name, type, amount, recipient] = regex.exec(instruction)
    if (!table[name]) {
        table[name] = {}
    }
    table[name][recipient] = type === 'gain' ? Number(amount) : -Number(amount)
}

input.split('\n').forEach(parse)

const combos = permute(Object.keys(table))

let max = 0
combos.forEach(names => {
    let total = 0
    for (let i = 0; i < names.length; i++) {
        if (i===0) {
            const a = names[names.length-1]
            const b = names[i]
            total += table[a][b]+table[b][a]
        } else {
            const a = names[i-1]
            const b = names[i]
            total += table[a][b]+table[b][a]
        }
    }
    if (total > max) max = total
})
console.log(max)
