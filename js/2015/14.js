import {input} from '../puzzle-input.js'
console.log(input)

const reindeer = {}

const regex = /([a-zA-Z]*) [a-z ]* ([0-9]*)[a-z\/ ]*([0-9]*) [a-z, ]* *([0-9]*)/
input.split('\n').forEach(i => {
    const [_, name, speed, duration, rest] = regex.exec(i)
    reindeer[name] = {
        speed: Number(speed),
        duration: Number(duration),
        rest: Number(rest),
        distance: 0,
        isResting: false,
        restUntil: null,
    }
})

const totalDuration = 2503
let curSecond = 1

while (curSecond <= totalDuration) {
    // step each reindeer that are not resting
    Object.keys(reindeer).forEach(name => {
        const {isResting, speed} = reindeer[name]
        if (isResting) return
        reindeer[name].distance += speed
    })

    // set any reindeer to rest that need it
    Object.keys(reindeer).forEach(name => {
    })


    ++curSecond
}


console.log(reindeer)
