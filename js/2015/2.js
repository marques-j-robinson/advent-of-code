import {input, splitBy} from '../util.js'
import {
    nums,
    arraySum,
    areaSquare,
    perimeterSquare,
    surfaceAreaRectangularPrism,
    volumeRectangularPrism,
} from '../math.js'

const part2 = true

const boxes = splitBy(input, '\n').map(sides => {
    return nums(splitBy(sides, 'x'))
})

const sm = sides => {
    sides.sort((a, b) => a-b)
    return sides.slice(0, sides.length-1)
}

console.log(
    arraySum(boxes.map(sides => {
        const smSide = sm(sides)
        if (!part2) return areaSquare(smSide)+surfaceAreaRectangularPrism(sides)
        if (part2) return perimeterSquare(smSide)+volumeRectangularPrism(sides)
    }))
)
