import Promise from 'bluebird'
const fs = Promise.promisifyAll(require("fs"))
const day = 8

export default (async () => {
    const {solve} = await import(`./${day}.js`)
    const puzzleInput = (await fs.readFileAsync(`data/2015_${day}`)).toString().trim()
    const {p1, p2} = solve(puzzleInput)
    console.log('Part 1:', p1)
    console.log('Part 2:', p2)
})()
