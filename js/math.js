export const arraySum = arr => arr.reduce((acc, i) => acc+Number(i), 0)

export const surfaceAreaRectangularPrism = ([l, w, h]) => 2*l*w + 2*w*h + 2*h*l

export const areaSquare = sides => sides.reduce((acc, i) => acc*i, 1)
