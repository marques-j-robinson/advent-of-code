import {input} from '../puzzle-input.js'

const houses = Array(Number(input)/10+1).fill(0)
for (let elf = 1; elf < houses.length; elf++) {
    for (let house = elf; house < houses.length; house+=elf) {
        houses[house] += elf*10
    }
}

for (let house = 1; house < houses.length; house++) {
    if (houses[house] > Number(input)) {
        console.log(house)
        break
    }
}
