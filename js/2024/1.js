import {input} from '../puzzle-input.js'
import {sum} from '../array.js'

function sortLeastToGreatest(list) {
    list.sort((a, b) => a - b)
}

function seperateLists() {
    const listA = []
    const listB = []

    input.split('\n').forEach(i => {
        const [a, b] = i.split(/\s+/)
        listA.push(a)
        listB.push(b)
    })

    sortLeastToGreatest(listA)
    sortLeastToGreatest(listB)

    return [listA, listB]
}

const [a, b] = seperateLists()

const diffs = []

a.forEach((i, idx) => {
    diffs.push(Math.abs(i-b[idx]))
})

console.log(sum(diffs))
