import {input} from '../puzzle-input.js'
import {sum} from '../array.js'
import {
    nums,
    areaSquare,
    perimeterSquare,
    surfaceAreaRectangularPrism,
    volumeRectangularPrism,
} from '../math.js'

const part2 = true

const boxes = input.split('\n').map(sides => {
    return nums(sides.split('x'))
})

const sm = sides => {
    sides.sort((a, b) => a-b)
    return sides.slice(0, sides.length-1)
}

console.log(
    sum(boxes.map(sides => {
        const smSide = sm(sides)
        if (!part2) return areaSquare(smSide)+surfaceAreaRectangularPrism(sides)
        if (part2) return perimeterSquare(smSide)+volumeRectangularPrism(sides)
    }))
)
