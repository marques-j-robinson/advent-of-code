import { input } from '../puzzle-input.js'
import { nums } from '../math.js'

const part2 = true

const list = nums(input.split(''))

const getHalfwayIndex = (idx) => {
  const offset = Math.floor(list.length / 2)
  return (idx + offset) % list.length
}

const getPair = (idx) => {
  if (part2) {
    return [list[idx], list[getHalfwayIndex(idx)]]
  } else {
    if (idx === list.length - 1) {
      return [list[idx], list[0]]
    }
    return [list[idx], list[idx + 1]]
  }
}

const checkMatch = (arr) => arr[0] === arr[1]

let total = 0

list.forEach((item, idx) => {
  if (checkMatch(getPair(idx))) total += item
})

console.log(total)
