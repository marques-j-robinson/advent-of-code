import {input} from '../util.js'
import {arraySum} from '../math.js'

const part2 = true

const getId = s => s.match(/Game (\d*)/)[1]
const formatCubes = s => s.match(/: (.*)/)[1].split('; ').map(i => i.split(', '))

const games = input.split('\n').map(game => ({
    id: getId(game),
    cubePulls: formatCubes(game),
}))

const play = ({id, cubePulls}) => {
    let isValid = true
    let red =  0
    let green =  0
    let blue =  0
    cubePulls.forEach(cubes => {
        cubes.forEach(c => {
            const [n, cube] = c.split(' ')
            if (part2) {
                if (cube === 'red' && n > red) red = Number(n)
                if (cube === 'green' && n > green) green = Number(n)
                if (cube === 'blue' && n > blue) blue = Number(n)
            } else {
                if (cube === 'red' && n > 12) isValid = false
                if (cube === 'green' && n > 13) isValid = false
                if (cube === 'blue' && n > 14) isValid = false
            }
        })
    })
    return part2
        ? red*green*blue
        : isValid && id
}

console.log(arraySum(games.map(play).filter(i => i)))
