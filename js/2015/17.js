import {input} from '../puzzle-input.js'
import {sum, combination} from '../array.js'

const containers = input.split('\n').map(i => Number(i))

const amountOfEggnog = 150

let total = 0
for (let n of combination(containers)) {
    if (sum(n) === amountOfEggnog) total += 1
}

console.log(total)
