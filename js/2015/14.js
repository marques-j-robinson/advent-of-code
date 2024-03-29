import {input} from '../puzzle-input.js'

const part2 = true

const reindeer = {}

const regex = /([a-zA-Z]*) [a-z ]* ([0-9]*)[a-z\/ ]*([0-9]*) [a-z, ]* *([0-9]*)/
input.split('\n').forEach(i => {
    const [_, name, speed, duration, rest] = regex.exec(i)
    reindeer[name] = {
        speed: Number(speed),
        duration: Number(duration),
        rest: Number(rest),
        distance: 0,
        cur: 0,
        isResting: false,
    }
    part2 ? reindeer[name].points = 0 : null
})

const totalDuration = 2503
let curSecond = 1

/*
 * Stepping
 * All reindeer that can step do, then any that must rest are set to rest
 * Any reindeer that are resting and are ready to step need to be told to step for the next iteration
 *
 * Note about Part 2:
 * After stepping, any reindeer that are in the lead are given a point
 */

function toggleRestStatus(name) {
    reindeer[name].cur = 0
    reindeer[name].isResting = !reindeer[name].isResting
}

function step(name) {
    reindeer[name].cur += 1
    
    if (!reindeer[name].isResting) {
        reindeer[name].distance += reindeer[name].speed
        if (reindeer[name].duration === reindeer[name].cur) {
            toggleRestStatus(name)
        }
    } else {
        if (reindeer[name].rest === reindeer[name].cur) {
            toggleRestStatus(name)
        }
    }
}

function assignLeadPoints() {
    let max = null
    Object.keys(reindeer).forEach(name => {
        if (reindeer[name].distance > max) {
            max = reindeer[name].distance
        }
    })
    const leaders = []
    Object.keys(reindeer).forEach(name => {
        if (reindeer[name].distance === max) {
            leaders.push(name)
        }
    })
    leaders.forEach(name => {
        reindeer[name].points += 1
    })
}

while (curSecond <= totalDuration) {
    Object.keys(reindeer).forEach(step)
    part2 ? assignLeadPoints() : null
    ++curSecond
}

function getWinner() {
    let winner = null
    Object.keys(reindeer).forEach(name => {
        if (part2) {
            if (reindeer[name].points > winner) {
                winner = reindeer[name].points
            }
        } else {
            if (reindeer[name].distance > winner) {
                winner = reindeer[name].distance
            }
        }
    })
    return winner
}

console.log(getWinner())