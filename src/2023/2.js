import {input, splitByLine, sum} from '../util.js'

const gameData = s => s.match(/: (.*)/)[1]
const gameId = s => s.match(/Game (\d*)/)[1]

console.log(sum(
    splitByLine(input).map(l => {
        let isValid = true
        gameData(l).split('; ').map(cubes => {
            cubes.split(', ').forEach(c => {
                const [n, cube] = c.split(' ')
                if (cube === 'red' && n > 12) isValid = false
                if (cube === 'green' && n > 13) isValid = false
                if (cube === 'blue' && n > 14) isValid = false
            })
        })
        if (isValid) return gameId(l)
    }).filter(i => i)
))

console.log(sum(
    splitByLine(input).map(l => {
        let red =  0
        let green =  0
        let blue =  0
        gameData(l).split('; ').map(cubes => {
            cubes.split(', ').forEach(c => {
                const [n, cube] = c.split(' ')
                if (cube === 'red' && n > red) red = Number(n)
                if (cube === 'green' && n > green) green = Number(n)
                if (cube === 'blue' && n > blue) blue = Number(n)
            })
        })
        return red*green*blue
    })
))
