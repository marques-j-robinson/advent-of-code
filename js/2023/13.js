import {input} from '../util.js'
import {sum} from '../array.js'

// data formatting
const patterns = input.split('\n\n')
const rows = patterns.map(i => i.split('\n'))
const columns = rows.map(row => {
    const cols = []
    let i = 0
    while (i<row[0].length) {
        cols.push(row.map(r => r[i]).join(''))
        ++i
    }
    return cols
})

// checks/validators
const horizontal = id => {
    let isValid = true
    const arr = rows[id]
    let rowsAbove = 0
    let prev = 0
    let cur = 1
    while (cur<arr.length) {
        if (rowsAbove !== 0 && arr[prev] !== arr[cur]) {
            isValid = false
            break
        }
        if (arr[prev] === arr[cur]) {
            if (rowsAbove === 0) rowsAbove = cur
            --prev
        } else {
            ++prev
        }
        ++cur
    }
    if (!isValid) return 0
    return rowsAbove*100
}

const vertical = id => {
    let isValid = true
    const arr = columns[id]
    let numCols = 0
    let prev = 0
    let cur = 1
    while (cur<arr.length) {
        if (numCols !== 0 && arr[prev] !== arr[cur]) {
            isValid = false
            break
        }
        if (arr[prev] === arr[cur]) {
            if (numCols === 0) numCols = cur
            --prev
        } else {
            ++prev
        }
        ++cur
    }
    if (!isValid) return 0
    return numCols
}

// core operation
let pId = 0
let total = 0

while (pId<patterns.length) {
    total += horizontal(pId)
    total += vertical(pId)
    ++pId
}

console.log(total)

//const isMatch = (a, b) => {
    //let count = 0
    //for (let i = 0; i<a.length; ++i) {
        //if (a[i] === b[i]) ++count
    //}
    //return count === a.length
//}

//const horizontal = pattern => {
    //let valid = true
    //let prev = 0
    //let cur = 1

    //while (cur<pattern.length) {
        //if (isMatch(pattern[prev], pattern[cur])) break

        //++prev
        //++cur
    //}
    //if (cur === pattern.length) return 0
    //const res = cur

    //prev -= 1
    //cur += 1

    //while (cur<pattern.length && prev>=0) {
        //if (!isMatch(pattern[prev], pattern[cur])) valid = false

        //--prev
        //++cur
    //}

    //if (!valid) return 0
    //return res*100
//}

//const vertical = pattern => {
    //let valid = true
    //let prev = 0
    //let cur = 1

    //while (cur<pattern[0].length) {
        //if (isMatch(pattern.map(i => i[prev]), pattern.map(i => i[cur]))) break

        //++prev
        //++cur
    //}
    //if (cur === pattern[0].length) return 0
    //const res = cur

    //prev -= 1
    //cur += 1

    //while (cur<pattern.length && prev>=0) {
        //if (!isMatch(pattern.map(i => i[prev]), pattern.map(i => i[cur]))) valid = false

        //--prev
        //++cur
    //}

    //if (!valid) return 0
    //return res
//}

//console.log(sum(patterns.map(p => horizontal(p)+vertical(p))))
