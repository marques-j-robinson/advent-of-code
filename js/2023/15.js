import {input} from '../util.js'
import {sum} from '../array.js'
const steps = input.split(',')

const part2 = true

const hash = str => {
    let total = 0
    str.split('').forEach(s => {
        total += s.charCodeAt(0)
        total = (total*17)%256
    })
    return total
}

const parse = str => str.match(/([a-z]*)([\=\-])(\d*)/)

if (!part2) console.log(sum(steps.map(hash)))
if (part2) {
    const boxes = {}
    steps.forEach(step => {
        const [_, label, op, v] = parse(step)
        const val = Number(v)
        const boxId = hash(label)
        if (op === '-' && boxes[boxId]) {
            boxes[boxId] = boxes[boxId].filter(i => i.label !== label)
            if (boxes[boxId].length === 0) delete boxes[boxId]
        }
        if (op === '=') {
            if (!boxes[boxId]) boxes[boxId] = []
            if (boxes[boxId].filter(i => i.label === label).length === 0) {
                boxes[boxId].push({label, val})
            } else {
                boxes[boxId].forEach(i => {
                    if (i.label === label) i.val = val
                })
            }
        }
    })
    console.log(sum(Object.keys(boxes).map(key => {
        let total = 0
        boxes[key].forEach(({val}, slot) => {
            total += (1+Number(key))*(1+Number(slot))*val
        })
        return total
    })))
}
