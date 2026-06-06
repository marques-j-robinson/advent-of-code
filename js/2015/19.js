import {input} from '../puzzle-input.js'
const [replacements, medicine] = input.split('\n\n')
const parse = i => i.split(' => ')

const distinct = []

replacements.split('\n').forEach(r => {
    const [toFind, replace] = parse(r)

    for (let i = 0; i<medicine.length; i++) {
        let letters
        if (toFind.length === 1) {
            letters = medicine[i]
        } else {
            letters = medicine.substring(i, i+toFind.length)
        }
        if (toFind === letters) {
            const first = medicine.slice(0, i)
            const last = medicine.slice(i+toFind.length)
            const newMolecule = first+replace+last
            if (!distinct.includes(newMolecule)) {
                distinct.push(newMolecule)
            }
        }
    }
})

console.log(distinct.length)
