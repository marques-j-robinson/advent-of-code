import { input } from '../puzzle-input.js'
import { nums } from '../math.js'

const part2 = true

const rows = input.split('\n').map((i) => nums(i.split('\t')))

const checkSum = rows.reduce((acc, row) => {
  if (!part2) {
    const largest = Math.max(...row)
    const smallest = Math.min(...row)
    const difference = largest - smallest
    return acc + difference
  }
  let quotient = 0
  outerloop: for (let i = 0; i < row.length; i++) {
    const cur = row[i]
    for (let j = i + 1; j < row.length; j++) {
      const next = row[j]
      if (cur % next === 0) {
        quotient = cur / next
        break outerloop
      }
      if (next % cur === 0) {
        quotient = next / cur
        break outerloop
      }
    }
  }
  return acc + quotient
}, 0)
console.log(checkSum)
