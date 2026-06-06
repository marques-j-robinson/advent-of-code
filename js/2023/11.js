import {input} from '../util.js'
import {sum, pairs} from '../array.js'
import {manhattanDistance} from '../math.js'

const space = input.split('\n').map(i => i.split(''))

const expandColumns = () => {
    const colLength = space[0].length
    let colId = 0
    while (colId <= colLength) {
        let valid = true
        space.forEach(row => {
            if (row[colId] !== '.') valid = false
        })
        if (valid) {
            space.forEach(row => row.splice(colId, 0, '.'))
            ++colId
        }
        ++colId
    }
}

const expandRows = () => {
    const emptyRow = [...Array(space[0].length)].map(i => '.')
    const emptyRows = []
    space.forEach((row, rowIdx) => {
        let valid = true
        row.forEach(col => {
            if (col !== '.') valid = false
        })
        if (valid) emptyRows.push(rowIdx)
    })
    emptyRows.forEach(rowIdx => {
        space.splice(rowIdx+1, 0, emptyRow)
    })
}

expandColumns()
expandRows()
console.log(space.map(i => i.join('')))

const galaxies = []
space.forEach((row, rowId) => row.forEach((col, colId) => {
    if (col !== '.') {
        galaxies.push({x:rowId, y:colId})
    }
}))

console.log(sum(pairs(galaxies).map(([a, b]) => {
    const x = Math.abs(b.x-a.x)
    const y = Math.abs(b.y-a.y)
    return manhattanDistance(x, y)
})))
