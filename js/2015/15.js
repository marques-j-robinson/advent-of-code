import {input} from '../puzzle-input.js'

const part2 = false

const ingredients = input.split('\n').reduce((acc, i) => {
	const [_, name, properties] = /([a-zA-Z]*): ([0-9a-z,\s-]*)$/.exec(i)
	acc[name] = {}
	properties.split(', ').forEach(p => {
		const [propertyName, value] = p.split(' ')
		if (!part2 && propertyName === 'calories') return
		acc[name][propertyName] = Number(value)
	})
	return acc
}, {})

function teaspoonCombos() {
	const res = []

	const limit = 100
	function isTeaspoonLimit(a, b, c, d) {
		return a+b+c+d === limit
	}
	
	const nums = Array.from(Array(97), (_, index) => index + 1)
	const reversedNums = [...nums].reverse()

	reversedNums.forEach(a => {
		nums.forEach(b => {
			nums.forEach(c => {
				nums.forEach(d => {
					if (isTeaspoonLimit(a, b, c, d)) res.push([a, b, c, d])
				})
			})
		})
	})

	return res
}

function handleNegative(num) {
	return num < 0 ? 0 : num
}

let max = 0
teaspoonCombos().forEach(teaspoons => {
	let capacity = 0
	let durability = 0
	let flavor = 0
	let texture = 0
	Object.keys(ingredients).forEach((name, key) => {
		const teaspoon = teaspoons[key]
		capacity += teaspoon*ingredients[name].capacity
		durability += teaspoon*ingredients[name].durability
		flavor += teaspoon*ingredients[name].flavor
		texture += teaspoon*ingredients[name].texture
	})
	const total = handleNegative(capacity)*handleNegative(durability)*handleNegative(flavor)*handleNegative(texture)
	if (total > max) max = total
})
console.log(max)