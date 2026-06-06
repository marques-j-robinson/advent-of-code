import {input} from '../puzzle-input.js'
import {nums} from '../math.js'

const reports = input.split('\n')

const safeReports = reports.filter(report => {
    const levels = nums(report.split(' '))

    let isSafe = true
    let type = null

    //console.log(levels)

    levels.forEach((current, idx) => {
        if (!isSafe) return
        if (idx === 0) {
            const next = levels[idx+1]
            if (current < next) {
                type = 'asc'
            } else if (current > next) {
                type = 'desc'
            }
        } else if (idx > 0 && idx < levels.length) {
            const next = levels[idx+1]
            if (type === 'desc') {
                if (current <= next || current-next > 3) {
                    isSafe = false
                }
            } else if (type === 'asc') {
                if (current >= next || next-current > 3) {
                    isSafe = false
                }
            }
        }
    })

    if (!isSafe) {
        console.log(levels)
    }

    return isSafe
})

console.log(safeReports.length)
