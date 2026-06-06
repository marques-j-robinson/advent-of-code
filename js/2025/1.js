import {input} from '../puzzle-input.js'

function translateInputByRotation(lines) {
    return lines.map(i => {
        const prefix = i[0] === 'R' ? '' : '-'
        return Number(`${prefix}${i.slice(1)}`)
    })
}

function prepInput(i) {
    const inputSplitByNewLine = i.split('\n')
    return translateInputByRotation(inputSplitByNewLine)
}

const instructions = prepInput(input)
console.log(instructions)

const startingPoint = 50
const min = 0
const max = 99

let solution = 0
let point = startingPoint
/*
lines.forEach(distance => {
    point = point + distance
    if (point < 0) {
        point = point+max+1
    } else if (point > max) {
        point = point-max-1
    }
    if (point === 0) {
        total += 1
    }
})

console.log(point)
console.log(total)
*/
