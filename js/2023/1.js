import {input} from '../util.js'
import {arraySum} from '../math.js'

const part2 = true

const numWords = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

const append = word => word[0]+numWords[word]+word[word.length-1]

const replaceNumWords = lines => lines.map(s => {
    let newStr = s
    Object.keys(numWords).forEach(word => {
        newStr = newStr.replaceAll(word, append(word))
    })
    return newStr
})

const calibrate = lines => lines.map(s => {
    const n = s.replaceAll(/\D/g, '')
    return `${n[0]}${n[n.length-1]}`
})

const lines = input.split('\n')

console.log(
    arraySum(part2?calibrate(replaceNumWords(lines)):calibrate(lines))
)
