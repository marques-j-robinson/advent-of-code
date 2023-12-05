import {input, splitByLine} from '../util.js'
import {
    arraySum,
    areaSquare,
    surfaceAreaRectangularPrism,
} from '../math.js'

const sm = arr => {
    arr.sort((a, b) => a-b)
    return arr.slice(0, arr.length-1)
}

console.log(arraySum(splitByLine(input).map(sides => sides.split('x').map(Number))
    .map(sides => areaSquare(sm(sides))+surfaceAreaRectangularPrism(sides))))
