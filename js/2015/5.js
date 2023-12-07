import {input} from '../util.js'
import {arraySum} from '../math.js'
import {
    hasVowelCount,
    noForbiddenVals,
    hasDupLetters,
    hasLetterPair,
    doLettersRepeat,
} from '../string-validation.js'

const part2 = true

const forbidden = ['ab', 'cd', 'pq', 'xy']

console.log(
    arraySum(input.split('\n').map(letters => {
        if (!part2) {
            return hasDupLetters(letters)
                && hasVowelCount(letters, 3)
                && noForbiddenVals(letters, forbidden)
                ? 1 : 0
        }
        if (part2) {
            return hasLetterPair(letters) && doLettersRepeat(letters, 3) ? 1 : 0
        }
    }))
)
