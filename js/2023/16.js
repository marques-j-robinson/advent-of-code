import {input} from '../puzzle-input.js'

// Format input like a grid
const grid = input.split('\n').map(i => i.split(''))
const colMax = grid[0].length-1
const rowMax = grid.length-1

/*
 * Traverse input like a grid, keeping track of all unique locations visited.
 * Direction is important and able to change based on the value of the current location.
 *
 * May need to handle each beam individually.
 * Tracking its location until it goes no further.
 * When a beam is split, simply create another beam starting at the new location
 *
 * Movement is a universal action, all beams are processed during movement
 */

let beamId = 0
const beams = [{
    id: beamId,
    isActive: true,
    direction: '>',
    row: 0,
    col: 0,
}]
const seen = []
let seenLength = 0

const getActiveBeams = () => beams.filter(b => b.isActive)

const removeBeam = beamId => {
    const [beam] = beams.filter(({id}) => id===beamId)
    beam.isActive = false
}

const getCurrentLocation = ({row, col}) => grid[row][col]

const checkBoundry = ({row, col}) => (col>=0 && col<=colMax) && (row>=0 && row<=rowMax)

const addSeen = beam => {
    if (!checkBoundry(beam)) {
        removeBeam(beam.id)
        return
    }
    const {row, col} = beam
    const coord = `${row},${col}`
    if (!seen.includes(coord)) seen.push(coord)
}

const addBeam = (direction, row, col) => {
    ++beamId
    const newBeam = {
        id: beamId,
        isActive: true,
        direction,
        row,
        col,
    }
    addSeen(newBeam)
    beams.push(newBeam)
    return newBeam
}

const move = () => {
    seenLength = seen.length
    getActiveBeams().forEach(beam => {
        addSeen(beam)
        const loc = getCurrentLocation(beam)
        if (loc === '.') {
            // empty space, pass through
        } else if (loc === '/') {
            if (beam.direction === '^') {
                beam.direction = '>'
            } else if (beam.direction === 'v') {
                beam.direction = '<'
            } else if (beam.direction === '>') {
                beam.direction = '^'
            } else if (beam.direction === '<') {
                beam.direction = 'v'
            }
        } else if (loc === '\\') {
            if (beam.direction === '^') {
                beam.direction = '<'
            } else if (beam.direction === 'v') {
                beam.direction = '>'
            } else if (beam.direction === '>') {
                beam.direction = 'v'
            } else if (beam.direction === '<') {
                beam.direction = '^'
            }
        } else if (loc === '-') {
            if (beam.direction === '^') {
                addBeam('>', beam.row, beam.col+1)
                beam.direction = '<'
            } else if (beam.direction === 'v') {
                addBeam('>', beam.row, beam.col+1)
                beam.direction = '<'
            } else if (beam.direction === '>') {
                // empty space, pass through
            } else if (beam.direction === '<') {
                // empty space, pass through
            }
        } else if (loc === '|') {
            if (beam.direction === '^') {
                // empty space, pass through
            } else if (beam.direction === 'v') {
                // empty space, pass through
            } else if (beam.direction === '>') {
                addBeam('v', beam.row+1, beam.col)
                beam.direction = '^'
            } else if (beam.direction === '<') {
                addBeam('v', beam.row+1, beam.col)
                beam.direction = '^'
            }
        }
        if (beam.direction === '^') beam.row -= 1
        if (beam.direction === 'v') beam.row += 1
        if (beam.direction === '>') beam.col += 1
        if (beam.direction === '<') beam.col -= 1
        addSeen(beam)
    })
}

while (getActiveBeams().length > 0 && seenLength<=seen.length) {
    move()
    console.log(seen.length)
}

console.log(seen)
console.log(seen.length)
