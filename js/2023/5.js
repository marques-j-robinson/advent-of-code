import { input } from '../util.js'

const getSeeds = s => s.match(/seeds: ([\d ]*)/)[1].split(' ').map(i => Number(i))
const seeds = getSeeds(input)

const categories = s => Array.from(input.matchAll(/.* map:\n([\d \n]*)/g), m => m[1]).map(i => i.trim().split('\n').map(j => j.split(' ').map(n => Number(n))))

categories(input).forEach(c => {
    seeds.forEach((s, idx) => {
        c.filter(([_, src, len]) => s>=src&&s<src+len)
        .forEach(([dest, src]) => {
            seeds[idx] = dest+s-src
        })
    })
})

console.log(Math.min(...seeds))

const seedRanges = []
let srange = []
seeds.forEach((s, idx) => {
    srange.push(s)
    if (idx % 2!==0) {
        seedRanges.push(srange)
        srange = []
    }
})

const isSeedRanges = i => {
    let res = false
    seedRanges.forEach(([start, slen]) => {
        if (i>=start && i<start+slen) res = true
    })
    return res
}

let cur = 0
let exit
while (!exit) {
    let s = cur
    categories(input).reverse().forEach(c => {
        c.filter(([dest, src, len]) => s>=dest&&s<dest+len)
        .forEach(([dest, src]) => {
            s = src+s-dest
        })
    })
    if (isSeedRanges(s)) {
        exit = true
        break
    }
    ++cur
}
console.log(cur)
