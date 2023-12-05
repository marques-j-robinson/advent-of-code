import {
    input,
    splitByLine,
} from '../util.js'
//const input = `seeds: 79 14 55 13

//seed-to-soil map:
//50 98 2
//52 50 48

//soil-to-fertilizer map:
//0 15 37
//37 52 2
//39 0 15

//fertilizer-to-water map:
//49 53 8
//0 11 42
//42 0 7
//57 7 4

//water-to-light map:
//88 18 7
//18 25 70

//light-to-temperature map:
//45 77 23
//81 45 19
//68 64 13

//temperature-to-humidity map:
//0 69 1
//1 0 69

//humidity-to-location map:
//60 56 37
//56 93 4`

const getSeeds = s => s.match(/seeds: ([\d ]*)/)[1].split(' ').map(i => Number(i))
//const seeds = [getSeeds(input)[1]]
const seeds = getSeeds(input)

const categories = s => Array.from(input.matchAll(/.* map:\n([\d \n]*)/g), m => m[1]).map(i => splitByLine(i.trim()).map(j => j.split(' ').map(n => Number(n))))

categories(input).forEach(c => {
    seeds.forEach((s, idx) => {
        c.filter(sub => s>=sub[1]&&s<=sub[1]+sub[2]-1)
        .forEach(([dest, src, len]) => {
            seeds[idx] = dest+s-src
        })
    })
})

console.log(Math.min(...seeds))
