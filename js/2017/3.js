import { input } from '../puzzle-input.js'
import { manhattanDistance } from '../math.js'

let edge = 0
const edges = []
for (let i = 1; i <= input; i += 2) {
  edge = i ** 2
  edges.push(edge)
  if (edge >= input) {
    break
  }
}

const level = edges.length - 1

console.log(manhattanDistance(level, level - (edge - input)))
