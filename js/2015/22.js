import { input } from '../puzzle-input.js'
const boss = {
  name: 'boss',
}
input.split('\n').forEach((i) => {
  const [name, value] = i.split(': ')
  if (name === 'Hit Points') boss['hp'] = Number(value)
  if (name === 'Damage') boss['damage'] = Number(value)
})
console.log(boss)

function game(players) {
  let id = 0

  const shouldPlay = () => players.filter(({ hp }) => hp > 0).length === 2

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
  players.forEach(({ hp, name }) => (hp > 0 ? (winner = name) : null))

  return winner
}
