import { input } from '../puzzle-input.js'
import { nums } from '../math.js'

const rows = input.split('\n').map((i) => nums(i.split('\t')))
const checkSum = rows.reduce((acc, row) => {
  const largest = Math.max(...row)
  const smallest = Math.min(...row)
  const difference = largest - smallest
  return acc + difference
}, 0)
console.log(checkSum)
