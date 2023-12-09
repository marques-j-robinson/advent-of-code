import {input} from '../util.js'
import {nums, arraySum} from '../math.js'

const getDiffs = history => {
    const diffs = [history]
    while (diffs[diffs.length-1].filter(i => i===0).length !== diffs[diffs.length-1].length) {
        const curDiff = diffs[diffs.length-1]
        let newDiffs = []
        for (let i = 1; i<curDiff.length; ++i) {
            newDiffs.push(curDiff[i]-curDiff[i-1])
        }
        diffs.push(newDiffs)
    }
    return diffs.reduce((acc, i) => {
        return acc+i[i.length-1]
    }, 0)
}

console.log(arraySum(input.split('\n').map(i => {
    return getDiffs(nums(i.split(' ')))
})))
