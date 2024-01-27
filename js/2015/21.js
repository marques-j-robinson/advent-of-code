import {input} from '../puzzle-input.js'

const shop = {
    weapons: [
        {
            name: 'Dagger',
            cost: 8,
            damage: 4,
            armor: 0,
        },
        {
            name: 'Shortsword',
            cost: 10,
            damage: 5,
            armor: 0,
        },
        {
            name: 'Warhammer',
            cost: 25,
            damage: 6,
            armor: 0,
        },
        {
            name: 'Longsword',
            cost: 40,
            damage: 7,
            armor: 0,
        },
        {
            name: 'Greataxe',
            cost: 74,
            damage: 8,
            armor: 0,
        },
    ],
    armor: [
        {
            name: 'Leather',
            cost: 13,
            damage: 0,
            armor: 1,
        },
        {
            name: 'Chainmail',
            cost: 31,
            damage: 0,
            armor: 2,
        },
        {
            name: 'Splintmail',
            cost: 53,
            damage: 0,
            armor: 3,
        },
        {
            name: 'Bandedmail',
            cost: 75,
            damage: 0,
            armor: 4,
        },
        {
            name: 'Platemail',
            cost: 102,
            damage: 0,
            armor: 5,
        },
    ],
    rings: [
        {
            name: 'Damage +1',
            cost: 25,
            damage: 1,
            armor: 0,
        },
        {
            name: 'Damage +2',
            cost: 50,
            damage: 2,
            armor: 0,
        },
        {
            name: 'Damage +3',
            cost: 100,
            damage: 3,
            armor: 0,
        },
        {
            name: 'Defense +1',
            cost: 20,
            damage: 0,
            armor: 1,
        },
        {
            name: 'Defense +2',
            cost: 40,
            damage: 0,
            armor: 2,
        },
        {
            name: 'Defense +3',
            cost: 80,
            damage: 0,
            armor: 3,
        },
    ],
}

function allShopOptions() {
    const res = []
    shop.weapons.forEach(weapon => {
        res.push([weapon])
    })
    shop.armor.forEach(a => {
        res.push([a])
    })
    shop.rings.forEach(ring => {
        res.push([ring])
    })
    shop.rings.forEach(ringA => {
        shop.rings.forEach(ringB => {
            if (ringA.name !== ringB.name) {
                res.push([ringA, ringB])
            }
        })
    })
    shop.weapons.forEach(weapon => {
        shop.armor.forEach(a => {
            res.push([weapon, a])
        })
    })
    shop.weapons.forEach(weapon => {
        shop.rings.forEach(ringA => {
            res.push([weapon, ringA])
            shop.rings.forEach(ringB => {
                if (ringA.name !== ringB.name) {
                    res.push([weapon, ringA, ringB])
                }
            })
        })
    })
    shop.armor.forEach(a => {
        shop.rings.forEach(ringA => {
            res.push([a, ringA])
            shop.rings.forEach(ringB => {
                if (ringA.name !== ringB.name) {
                    res.push([a, ringA, ringB])
                }
            })
        })
    })
    shop.weapons.forEach(weapon => {
        shop.armor.forEach(a => {
            shop.rings.forEach(ringA => {
                res.push([weapon, a, ringA])
                shop.rings.forEach(ringB => {
                    if (ringA.name !== ringB.name) {
                        res.push([weapon, a, ringA, ringB])
                    }
                })
            })
        })
    })
    return res
}

function game(players) {
    let id = 0

    const shouldPlay = () => players.filter(({hp}) => hp > 0).length === 2

    function fight(attacker, defender) {
        const amount = attacker.damage - defender.armor
        defender.hp -= amount <= 0 ? 1 : amount
    }


    while (shouldPlay()) {
        const attacker = players[id]
        id = +!id
        const defender = players[id]
        fight(attacker, defender)
    }

    let winner
    players.forEach(({hp, name}) => hp  > 0 ? winner = name : null)

    return winner
}

let cost = 100*100

allShopOptions().forEach(options => {
    const boss = {
        name: 'boss',
        // TEST DATA
        //hp: 12,
        //damage: 7,
        //armor: 2,
    }
    input.split('\n').forEach(i => {
        const [name, value] = i.split(': ')
        if (name === 'Hit Points') boss['hp'] = Number(value)
        if (name === 'Damage') boss['damage'] = Number(value)
        if (name === 'Armor') boss['armor'] = Number(value)
    })
    const player = {
        name: 'player',
        hp: 100,
        damage: 0,
        armor: 0,
        //TEST DATA
        //hp: 8,
        //damage: 5,
        //armor: 5,
    }
    options.forEach(({damage, armor}) => {
        player.damage += damage
        player.armor += armor
    })

    const winner = game([player, boss])
    console.log(winner)
    if (winner === 'player') {
        const optionsCost = options.reduce((acc, i) => acc+i.cost, 0)
        if (optionsCost < cost) cost = optionsCost
    }
})

console.log(cost)
