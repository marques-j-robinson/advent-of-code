import {input} from '../puzzle-input.js'

function parse() {
    const regex = /Sue ([0-9]*): (.*)$/

    return input.split('\n').map(i => {
        const [_, id, values] = regex.exec(i)
        return {
            id,
            values: values.split(', ').reduce((acc, v) => {
                const [name, value] = v.split(': ')
                acc[name] = Number(value)
                return acc
            }, {})
        }
    })
}

const sueList = parse()

const output = {
    children: 3,
    cats: 7,
    samoyeds: 2,
    pomeranians: 3,
    akitas: 0,
    vizslas: 0,
    goldfish: 5,
    trees: 3,
    cars: 2,
    perfumes: 1,
}

let match = null

sueList.forEach(({id, values}) => {
    let valid = true
    Object.keys(output).forEach(key => {
        if (values[key] && values[key] !== output[key]) valid = false
    })

    if (valid) match = id
})

console.log(match)
