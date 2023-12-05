import {input} from '../util.js'
let p1 = 0
let p2 = 0
let symbolRe = /[^.\d\n]/gm
let numRe = /\d*/g
let gearRe = /\*/g

const lines = input.split('\n')
const lineLen = lines[0].length

const nums = lines.flatMap((line, lineIdx) => {
    const matches = [...line.matchAll(numRe)]
    return matches.filter(i => i[0]!=='').map(i => {
        return {
            num: Number(i[0]),
            start: i.index,
            end: i.index+i[0].length-1,
            lineIdx,
        }
    })
})

const symbolsByLine = lines.map(line => {
    const matches = [...line.matchAll(symbolRe)]
    return matches.filter(i => i[0]!=='').map(i => i.index)
})

p1 += nums.map(({num, start, end, lineIdx}) => {
    let isValid = false
    //above
    if (lineIdx > 0) {
        const symbols = symbolsByLine[lineIdx-1]
        if (symbols.length) {
            if (start > 0 && symbols.includes(start-1)) isValid = true
            let i = start
            while (i<=end) {
                if (symbols.includes(i)) isValid = true
                ++i
            }
            if (end < lineLen && symbols.includes(end+1)) isValid = true
        }
    }
    //below
    if (lineIdx < lines.length-1) {
        const symbols = symbolsByLine[lineIdx+1]
        if (symbols.length) {
            if (start > 0 && symbols.includes(start-1)) isValid = true
            let i = start
            while (i<=end) {
                if (symbols.includes(i)) isValid = true
                ++i
            }
            if (end < lineLen && symbols.includes(end+1)) isValid = true
        }
    }
    //current
    const symbols = symbolsByLine[lineIdx]
    if (symbols.length) {
        if (start > 0 && symbols.includes(start-1)) isValid = true
        if (end < lineLen && symbols.includes(end+1)) isValid = true
    }
    return isValid && num
}).filter(i => i).reduce((acc, i) => acc+i, 0)

const gearsByLine = lines.map(line => {
    const matches = [...line.matchAll(gearRe)]
    return matches.filter(i => i[0]!=='').map(i => i.index)
})

p2 += gearsByLine.flatMap((line, lineIdx) => {
    return line.map(gIdx => {
        const gears = []
        let isValid = false
        //above
        if (lineIdx > 0) {
            nums.filter(n => n.lineIdx === lineIdx-1).forEach(({num, start, end}) => {
                if (gIdx > 0 && end === gIdx-1) gears.push(num)
                let i = start
                while (i<=end) {
                    if (i===gIdx) gears.push(num)
                    ++i
                }
                if (gIdx < lineLen && start === gIdx+1) gears.push(num)
            })
        }
        //below
        if (lineIdx < lines.length-1) {
            nums.filter(n => n.lineIdx === lineIdx+1).forEach(({num, start, end}) => {
                if (gIdx > 0 && end === gIdx-1) gears.push(num)
                let i = start
                while (i<=end) {
                    if (i===gIdx) gears.push(num)
                    ++i
                }
                if (gIdx < lineLen && start === gIdx+1) gears.push(num)
            })
        }
        //current
        nums.filter(n => n.lineIdx === lineIdx).forEach(({num, start, end}) => {
            if (gIdx > 0 && end === gIdx-1) gears.push(num)
            if (gIdx < lineLen && start === gIdx+1) gears.push(num)
        })
        if (gears.length === 2) {
            return gears.reduce((acc, i) => acc*i, 1)
        }
    })
}).filter(i => i).reduce((acc, i) => acc+i, 0)

console.log(p1)
console.log(p2)
