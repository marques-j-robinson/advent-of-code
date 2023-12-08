export const nums = arr => arr.map(Number)

export const arraySum = arr => nums(arr).reduce((acc, i) => acc+i, 0)
export const arrayProduct = arr => nums(arr).reduce((acc, i) => acc*i, 1)

export const surfaceAreaRectangularPrism = ([l, w, h]) => 2*l*w + 2*w*h + 2*h*l

export const volumeRectangularPrism = ([l, w, h]) => l*w*h

export const areaSquare = sides => sides.reduce((acc, i) => acc*i, 1)
export const perimeterSquare = sides => sides.reduce((acc, i) => acc+i*2, 0)

export const manhattanDistance = (a, b) => Math.abs(a) + Math.abs(b)

export const gcd = (a, b) => a ? gcd(b % a, a) : b;

export const lcm = (a, b) => a * b / gcd(a, b);
