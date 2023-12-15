import {input} from '../util.js'
import {sum} from '../array.js'

const part2 = true

const tilt = arr => {
    let colId = 0
    while (colId < arr[0].length) {
        let rowId = 0
        let edge = rowId
        while (rowId < arr.length-1) {
            const cur = arr[rowId][colId]
            const next = arr[rowId+1][colId]
            if (cur === 'O' || cur === '#') {
                edge = rowId+1
            }
            if (cur === '.' && next === 'O') {
                arr[edge][colId] = 'O'
                edge = edge+1
                arr[rowId+1][colId] = '.'
            }
            ++rowId
        }
        ++colId
    }
    return arr
}

const totalLoad = arr => sum(arr.reverse().map((row, rowId) => {
    let count = 0
    row.forEach(i => i === 'O' ? ++count : null)
    return count*(rowId+1)
}))

const rotate = arr => {
    const newArr = []
    let col = 0
    while (col<arr[0].length) {
        const newRow = []
        arr.forEach(r => {
            newRow.push(r[col])
        })
        newArr.push(newRow)
        ++col
    }
    return newArr
}

const rows = input.split('\n').map(i => i.split(''))
const display = arr => console.log(arr.map(i => i.join('')).join('\n'))

if (!part2) {
    console.log(totalLoad(tilt(rows)))
} else {
    const max = 1000
    let r = rows
    let i = 0
    while (i<max) {
        const cycleAmount = 4
        let count = 0
        while (count<cycleAmount) {
            r = tilt(r)
            r = rotate(r.reverse())
            ++count
        }
        ++i
    }
    console.log(totalLoad(r))
}
