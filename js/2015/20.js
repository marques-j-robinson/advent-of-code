import {input} from '../puzzle-input.js'

const part2 = true

if (!part2) {
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
}

const houses = Array(Number(input)/10+1).fill(0)
for (let elf = 1; elf < houses.length; elf++) {
    for (let house = elf, n = 0; house < houses.length && n < 50; house+=elf, n++) {
        houses[house] += elf*11
    }
}

for (let house = 1; house < houses.length; house++) {
    if (houses[house] > Number(input)) {
        console.log(house)
        break
    }
}
