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
    let rowId = 0
    while (rowId < arr.length) {
        arr[rowId].forEach((val, key) => {
            if (rowId === 0) {
                newArr.push([val])
            } else {
                newArr[key].push(val)
            }
        })
        ++rowId
    }
    return newArr
}

const rows = input.split('\n').map(i => i.split(''))

if (!part2) {
    console.log(totalLoad(tilt(rows)))
} else {
    const max = 1000000000
    let r = rows
    let i = 0
    while (i<max) {
        const cycleAmount = 4
        let count = 0
        while (count<cycleAmount) {
            r = rotate(tilt(r.reverse()))
            ++count
        }
        if (i%100000===0) console.log(i)
        ++i
    }
    console.log(totalLoad(rotate(r)))
}
