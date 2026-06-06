import {input} from '../puzzle-input.js'

// Example [["S", "7"], ["L", "J"]]
const grid = input.split('\n').map(r => r.split('').map(i => i))

/*
 * Worker
 *
 * Fn that accepts a current positional coordinate value,
 * returning two new values which both connect to the current position.
 */

function worker({row, col}) {
    const cur = grid[row][col]
    console.log(cur)

    const rows = [row, row+1, row-1]
    const cols = [col, col+1, col-1]
    rows.forEach(r => {
        cols.forEach(c => {
            if (row===r&&col===c) return
            console.log(`${r},${c}`)
            console.log(grid[r][c])
        })
    })

    return [
        //prev,
        //next,
    ]
}

/*
 * Stepping
 *
 * System in which "workers" connect pipes.
 * When "workers" arrive at the same current position hault stepping.
 * Total number of steps should be the correct answer to Part 1.
 */

const findStartPoint = () => {
    let startPoint
    grid.forEach((row, rowIdx) => {
        row.forEach((val, colIdx) => {
            if (val === 'S') startPoint = {row: rowIdx, col: colIdx}
        })
    })
    return startPoint
}

worker(findStartPoint())
