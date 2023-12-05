import {input} from '../util.js'

const formatNumbers = s => {
    return s.trim().replaceAll(' ', ',').split(',').filter(i => i).map(i => Number(i))
}

const getWinningNumbers = s => formatNumbers(s.match(/^.*:([\d\s]*)|/)[1])
const getAvailableNumbers = s => formatNumbers(s.match(/^.*\|([\d\s]*)/)[1])
const getCardNumber = s => Number(s.match(/^.*\s([\d]*):/)[1])

const processCount = n => {
    if (n === 0) return 0
    if (n === 1) return 1
    let res = 1
    let i = 1
    while (i<n) {
        res = res*2
        ++i
    }
    return res
}

const cards = []

const addCards = (startCardNum, total) => {
    if (!cards[startCardNum]) {
        cards[startCardNum] = 1
        let curCardNum = startCardNum+1
        let count = 0
        while (count<total) {
            cards[curCardNum] = 1
            curCardNum += 1
            ++count
        }
    } else {
        cards[startCardNum] += 1
        for (let i = 0; i<cards[startCardNum]; i++) {
            let curCardNum = startCardNum+1
            let count = 0
            while (count<total) {
                if (!cards[curCardNum]) {
                    cards[curCardNum] = 1
                } else {
                    cards[curCardNum] += 1
                }
                curCardNum += 1
                ++count
            }
        }
    }
}

let p1 = 0
let p2 = 0

let count = 0
input.split('\n').forEach(line => {
    let count = 0
    const added = []
    const cardNumber = getCardNumber(line)-1
    const win = getWinningNumbers(line)
    const avail = getAvailableNumbers(line)
    avail.forEach(n => {
        if (!added.includes(n) && win.includes(n)) {
            count += 1
            added.push(n)
        }
    })
    p1 += processCount(count)
    addCards(cardNumber, count)
})
p2 = cards.reduce((acc, i) => acc+i, 0)
console.log(p1)
console.log(p2)
