import {input} from '../puzzle-input.js'
let grid = input.split('\n').map(i => i.split(''))

const on = '#'
const off = '.'

const isOn = light => light === '#'
const isOff = light => light === '.'

function numNeighborsOn(neighbors) {
    return neighbors.reduce((acc, light) => {
        if (isOn(light)) acc+=1
        return acc
    }, 0)
}

function toggle(light, neighbors) {
    const neighborsOnCount = numNeighborsOn(neighbors)
    if (isOn(light) && (neighborsOnCount === 2 || neighborsOnCount === 3)) {
        return on
    } else if (isOff(light) && neighborsOnCount === 3) {
        return on
    } else {
        return off
    }
}

function getNeighbors(grid, rowId, colId) {
    const maxRow = grid.length-1
    const maxCol = grid[0].length-1

    const neighbors = []

    //left
    if (colId > 0) {
        neighbors.push(grid[rowId][colId-1])
        if (rowId > 0) {
            neighbors.push(grid[rowId-1][colId-1])
        }
        if (rowId < maxRow) {
            neighbors.push(grid[rowId+1][colId-1])
        }
    }

    //above
    if (rowId > 0) {
        neighbors.push(grid[rowId-1][colId])
    }

    //below
    if (rowId < maxRow) {
        neighbors.push(grid[rowId+1][colId])
    }

    //right
    if (colId < maxCol) {
        neighbors.push(grid[rowId][colId+1])
        if (rowId > 0) {
            neighbors.push(grid[rowId-1][colId+1])
        }
        if (rowId < maxRow) {
            neighbors.push(grid[rowId+1][colId+1])
        }
    }

    return neighbors
}

function processLights() {
    const newGrid = JSON.parse(JSON.stringify(grid))
    grid.forEach((row, rowId) => {
        row.forEach((col, colId) => {
            const neighbors = getNeighbors(grid, rowId, colId)
            newGrid[rowId][colId] = toggle(grid[rowId][colId], neighbors)
        })
    })
    grid = newGrid
}

const stepLimit = 100
let step = 0

while (step < stepLimit) {
    processLights()
    ++step
}

function getOnCount() {
    let count = 0
    grid.forEach((row, rowId) => {
        row.forEach(light => {
            if (isOn(light)) count += 1
        })
    })
    return count
}

console.log(getOnCount())
