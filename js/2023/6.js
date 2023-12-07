import {input} from '../util.js'
import {arrayProduct} from '../math.js'
const i = input.trim().split('\n').map(i => i.match(/([\d]*)/g).filter(i => i).map(i => Number(i)))
const times = i[0]
const distanceRecords = i[1]

const race = (time, distance) => {
    let winCount = 0
    let holdTime = 1
    while (holdTime < time) {
        const travelTime = time-holdTime
        if (holdTime*travelTime > distance) ++winCount
        ++holdTime
    }
    return winCount
}

const wins = []
times.forEach((t, idx) => {
    const d = distanceRecords[idx]
    wins.push(race(t, d))
})
console.log(arrayProduct(wins))

const time = Number(times.join(''))
const distance = Number(distanceRecords.join(''))
console.log(race(time, distance))
