import {input, splitByLine} from '../util.js'
const i = splitByLine(input.trim()).map(i => i.match(/([\d]*)/g).filter(i => i).map(i => Number(i)))
const times = i[0]
const distanceRecords = i[1]

const allAttempts = []

times.forEach((totalTime, idx) => {
    const distanceRecord = distanceRecords[idx]

    let validAttempts = 0
    let holdTime = 1
    while (holdTime < totalTime) {
        const travelTime = totalTime-holdTime
        const distance = holdTime*travelTime
        if (distance > distanceRecord) ++validAttempts
        ++holdTime
    }
    allAttempts.push(validAttempts)
})

console.log(allAttempts.reduce((acc, i) => acc*i, 1))
