import {input} from '../puzzle-input.js'

const ingredients = input.split('\n').reduce((acc, i) => {
	const [_, name, properties] = /([a-zA-Z]*): ([0-9a-z,\s-]*)$/.exec(i)
	acc[name] = {}
	properties.split(', ').forEach(p => {
		const [propertyName, value] = p.split(' ')
		acc[name][propertyName] = Number(value)
	})
	return acc
}, {})

/*
 * Dynamic teaspoon allocation
 * If the current teaspoon value is less than 25, (because and even distribution is 25)
 * then add 1 for the next iteration. Otherwise minus 1.
 */

function addTeaspoons() {}

console.log(ingredients)