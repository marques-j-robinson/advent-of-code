import {input} from '../util.js'
import {arraySum} from '../math.js'

const part2 = false

const strengthSortOrder = ['five', 'four', 'full_house', 'three', 'two_pair', 'one_pair', 'high']
const numCards = ['T', '9', '8', '7', '6', '5', '4', '3', '2']
const faceCards = ['A', 'K', 'Q']
const cardSortOrder = !part2 ? [...faceCards, 'J', ...numCards] : [...faceCards, ...numCards, 'J']

const formatBids = games => games.map((val, idx) => idx === 1 ? Number(val): val)
const games = input.split('\n').map(i => formatBids(i.split(' ')))


//const groupCards = hand => hand.split('').reduce((acc, i) => {
    //if (!acc[i]) {
        //acc[i] = 0
    //}
    //acc[i] += 1
    //return acc
//}, {})

//const getStrength = hand => {
    //if (hand === 'JJJJJ') return 'five'
    //const cards = groupCards(hand)
    //let high = 0
    //let highCard
    //const c = Object.keys(cards)
    //c.sort((a, b) => {
        //return cardSortOrder.indexOf(b) - cardSortOrder.indexOf(a)
    //})
    //c.forEach(i => {
        //if (cards[i] >= high && i!=='J') {
            //high = cards[i]
            //highCard = i
        //}
    //})
    //high = 0
    //let pairs = 0
    //const newCards = groupCards(hand.replaceAll('J', highCard))
    //Object.keys(newCards).forEach(i => {
        //if (newCards[i] > high) high = newCards[i]
        //if (newCards[i] === 2) pairs += 1
    //})
    //if (high === 1) return 'high'
    //if (high === 2 && pairs === 1) return 'one_pair'
    //if (high === 2 && pairs === 2) return 'two_pair'
    //if (high === 3 && pairs === 1) return 'full_house'
    //if (high === 3 && pairs === 0) return 'three'
    //if (high === 4) return 'four'
    //if (high === 5) return 'five'
//}

//const games = i.map(([hand, bid]) => ({
    //hand, bid,
    //strength: getStrength(hand),
//}))
//games.sort((a, b) => {
    //return strengthSortOrder.indexOf(a.strength) - strengthSortOrder.indexOf(b.strength)
//})

//games.sort((a, b) => {
    //if (a.strength === b.strength) {
        //for (let i = 0; i<a.hand.length; ++i) {
            //if (a.hand[i] !== b.hand[i]) {
                //return cardSortOrder.indexOf(a.hand[i]) - cardSortOrder.indexOf(b.hand[i])
                //break
            //}
        //}
    //}
//})
//console.table(games)
//console.log(arraySum(games.map((i, idx) => i.bid*(games.length-idx))))
