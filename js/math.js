export const arraySum = arr => arr.reduce((acc, i) => acc+Number(i), 0)

export const surfaceAreaRectangularPrism = ([l, w, h]) => 2*l*w + 2*w*h + 2*h*l

export const volumeRectangularPrism = ([l, w, h]) => l*w*h

export const areaSquare = sides => sides.reduce((acc, i) => acc*i, 1)
export const perimeterSquare = sides => sides.reduce((acc, i) => acc+i*2, 0)
