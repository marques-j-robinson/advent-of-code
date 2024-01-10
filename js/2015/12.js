import {input} from '../puzzle-input.js'

const part2 = true

let total = 0

function calculate(json) {
    if (typeof json === 'number') {
        total += json
        return
    }

    if (Array.isArray(json)) {
        json.forEach(calculate)
    }

    if (!Array.isArray(json) && typeof json === 'object') {
        if (part2 && Object.values(json).includes('red')) return
        Object.keys(json).forEach(k => {
            calculate(json[k])
        })
    }
}

calculate(JSON.parse(input))
console.log(total)
