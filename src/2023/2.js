import {input, splitByLine, sum} from '../util.js'

console.log(sum(
    splitByLine(input).map(l => {
        const [_, id, gameData] = l.match(/Game (\d*): (.*)/)
        let isValid = true
        gameData.split('; ').map(cubes => {
            cubes.split(', ').forEach(c => {
                const [n, cube] = c.split(' ')
                if (cube === 'red' && n > 12) isValid = false
                if (cube === 'green' && n > 13) isValid = false
                if (cube === 'blue' && n > 14) isValid = false
            })
        })
        if (isValid) return id
    }).filter(i => i)
))

console.log(sum(
    splitByLine(input).map(l => {
        let red =  0
        let green =  0
        let blue =  0
        l.match(/: (.*)/)[1].split('; ').map(cubes => {
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
