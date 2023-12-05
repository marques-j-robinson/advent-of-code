import {input, splitByLine} from '../util.js'
import {arraySum} from '../math.js'
const i = splitByLine(input)

const vowels = 'aeiou'
const minVowels = 3
const hasThreeVowels = letters => {
    let count = 0
    letters.split('').forEach(l => {
        if (vowels.includes(l)) {
            count += 1
        }
    })
    return count >= minVowels
}

const compairLetters = (a, b) => a === b

const hasDupLetters = letters => {
    let hasDup = false
    for (let idx = 0; idx <= letters.length-2; idx++) {
        const a = letters[idx]
        const b = letters[idx+1]
        if (compairLetters(a, b)) {
            hasDup = true
        }
    }
    return hasDup
}

const forbidden = ['ab', 'cd', 'pq', 'xy']
const noForbiddenVals = letters => {
    let isClean = true
    forbidden.forEach(f => {
        if (letters.includes(f)) {
            isClean = false
        }
    })
    return isClean
}

const createPairs = letters => {
    const pairs = []
    for (let idx = 0; idx <= letters.length-2; idx++) {
        const a = letters[idx]
        const b = letters[idx+1]
        pairs.push(`${a}${b}`)
    }
    return pairs
}

const hasLetterPair = letters => {
    let hasPair = false
    const pairs = createPairs(letters)
    pairs.forEach((curPair, pairId) => {
        for (let idx = pairId+2; idx <= pairs.length-1; idx++) {
            const nextPair = pairs[idx]
            if (compairLetters(curPair, nextPair)) {
                hasPair = true
            }
        }
    })
    return hasPair
}

const doLettersRepeat = letters => {
    let repeat = false
    for (let idx = 0; idx <= letters.length-3; idx++) {
        const a = letters[idx]
        const b = letters[idx+2]
        if (compairLetters(a, b)) {
            repeat = true
        }
    }
    return repeat
}

console.log(arraySum(i.map(letters => hasDupLetters(letters) && hasThreeVowels(letters) && noForbiddenVals(letters) ? 1 : 0)))
console.log(arraySum(i.map(letters => hasLetterPair(letters) && doLettersRepeat(letters) ? 1 : 0)))
