import {input} from '../puzzle-input.js'

const max = 7

const letters = 'abcdefghijklmnopqrstuvwxyz'.split('')
const n = letters.length

/*
 * Validation Functions
 */
const invalid = ['i', 'o', 'l']

const checkInvalidLetters = arr => {
    let res = true
    arr.forEach(l => {
        if (invalid.includes(l)) res = false
    })
    return res
}

const containsThreeLetterStraight = arr => {
    let res = false
    for (let i = 0; i <= arr.length-3; i++) {
        const a = letters.indexOf(arr[i])
        const b = letters.indexOf(arr[i+1])
        const c = letters.indexOf(arr[i+2])
        if (b-1 === a && c-2 === a) res = true
    }
    return res
}

const checkPairs = arr => {
    const pairs = []
    let count = 0
    for (let i = 0; i <= arr.length-2; i++) {
        const a = arr[i]
        const b = arr[i+1]
        const pair = `${a}${b}`
        if (a === b && !pairs.includes(pair)) {
            ++count
            pairs.push(pair)
        }
    }
    return count >= 2
}

function isValid(str) {
    const arr = str.split('')
    let res = true
    res = containsThreeLetterStraight(arr) && checkInvalidLetters(arr) && checkPairs(arr)
    return res
}

/*
 * Stepping
 */
const circular = i => letters[(i % n + n) % n]
const step = l => circular(letters.indexOf(l)+1)

let str = input

while (!isValid(str)) {
    const arr = str.split('')
    let i = str.length-1
    while (i>=0) {
        const cur = arr[i]
        arr[i] = step(cur)
        if (cur === 'z' && arr[i] === 'a') {
            --i
        } else {
            str = arr.join('')
            break
        }
    }
    str = arr.join('')
}

console.log(str)
