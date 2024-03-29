import { input } from '../puzzle-input.js'

const part2 = true

function process(incoming) {
    let outgoing = ''
    let i = 0
    while (i<incoming.length) {
        const cur = Number(incoming[i])
        let count = 0
        let j = i
        let exit = false
        while (!exit) {
            ++count
            ++j
            const next = Number(incoming[j])
            if (cur !== next) {
                exit = true
            }
        }
        outgoing += `${count}${cur}`
        i = j
    }
    return outgoing
}

let total = 0
let res = input
const max = part2 ? 50 : 40

while (total<max) {
    res = process(res)
    ++total
}

console.log(res.length)
