import { input } from '../puzzle-input.js'
import { nums } from '../math.js'

const list = nums(input.split(''))

const getPair = (idx) => {
  if (idx === list.length - 1) {
    return [list[idx], list[0]]
  }
  return [list[idx], list[idx + 1]]
}

const checkMatch = (arr) => arr[0] === arr[1]

let total = 0

list.forEach((item, idx) => {
  if (checkMatch(getPair(idx))) total += item
})

console.log(total)
