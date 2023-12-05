import {input, splitByLine} from '../util.js'
import {
    arraySum,
    areaSquare,
    perimeterSquare,
    surfaceAreaRectangularPrism,
    volumeRectangularPrism,
} from '../math.js'

const boxes = splitByLine(input).map(sides => sides.split('x').map(Number))

const sm = arr => {
    arr.sort((a, b) => a-b)
    return arr.slice(0, arr.length-1)
}

console.log(arraySum(boxes.map(sides => areaSquare(sm(sides))+surfaceAreaRectangularPrism(sides))))
console.log(arraySum(boxes.map(sides => perimeterSquare(sm(sides))+volumeRectangularPrism(sides))))
