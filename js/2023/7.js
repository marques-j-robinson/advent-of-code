import {input, splitByLine} from '../util.js'
import {arraySum} from '../math.js'
const i = splitByLine(input).map(i => i.split(' ').map((i, idx) => idx === 1 ? Number(i) : i))

const strengthSortOrder = ['five', 'four', 'full_house', 'three', 'two_pair', 'one_pair', 'high']
const cardSortOrder = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2', '1']

const groupCards = hand => hand.split('').reduce((acc, i) => {
    if (!acc[i]) {
        acc[i] = 0
    }
    acc[i] += 1
    return acc
}, {})

const getStrength = hand => {
    const cards = groupCards(hand)
    let high = 0
    let pairs = 0
    Object.keys(cards).forEach(i => {
        if (cards[i] > high) high = cards[i]
        if (cards[i] === 2) pairs += 1
    })
    if (high === 1) return 'high'
    if (high === 2 && pairs === 1) return 'one_pair'
    if (high === 2 && pairs === 2) return 'two_pair'
    if (high === 3 && pairs === 1) return 'full_house'
    if (high === 3 && pairs === 0) return 'three'
    if (high === 4 && pairs === 0) return 'four'
    if (high === 5 && pairs === 0) return 'five'
}

const games = i.map(([hand, bid]) => ({
    hand, bid,
    strength: getStrength(hand),
}))
games.sort((a, b) => {
    return strengthSortOrder.indexOf(a.strength) - strengthSortOrder.indexOf(b.strength)
})

games.sort((a, b) => {
    if (a.strength === b.strength) {
        for (let i = 0; i<a.hand.length; ++i) {
            if (a.hand[i] !== b.hand[i]) {
                return cardSortOrder.indexOf(a.hand[i]) - cardSortOrder.indexOf(b.hand[i])
                break
            }
        }
    }
})
console.log(arraySum(games.map((i, idx) => i.bid*(games.length-idx))))
