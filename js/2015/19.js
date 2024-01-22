import {input} from '../puzzle-input.js'
const [replacements, molecule] = input.split('\n\n')

const parse = i => i.split(' => ')

const distinct = []

replacements.split('\n').forEach(r => {
    const [toFind, replace] = parse(r)

    for (let i = 0; i<molecule.length; i++) {
        let letters
        if (toFind.length === 1) {
            letters = molecule[i]
        } else {
            letters = molecule.substring(i, i+toFind.length)
        }
        if (toFind === letters) {
            const first = molecule.slice(0, i)
            const last = molecule.slice(i+toFind.length)
            const newMolecule = first+replace+last
            if (!distinct.includes(newMolecule)) {
                distinct.push(newMolecule)
            }
        }
    }
})

console.log(distinct.length)
