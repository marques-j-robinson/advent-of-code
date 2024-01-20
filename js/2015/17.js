import {input} from '../puzzle-input.js'
import {sum, combination} from '../array.js'

const part2 = true

const containers = input.split('\n').map(i => Number(i))

const amountOfEggnog = 150

let min = containers.length
let total = 0
for (let n of combination(containers)) {
    if (sum(n) === amountOfEggnog) {
        if (!part2) {
            total += 1
        } else {
            if (n.length < min) {
                min = n.length
                total = 0
            }
            if (min === n.length) {
                total += 1
            }
        }
    }
}

console.log(total)
