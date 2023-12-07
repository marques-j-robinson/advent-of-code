import {input} from '../util.js'
const MAX_HEX_VALUE = 65535
let wires = {}
const resetWires = () => wires = {}

export const parseInstruction = i => {
    return {
        wire: i.match(/([a-z]*)$/)[0],
        sig: i.match(/^(.*) ->/)[1],
    }
}

export const convertToInt = i => Number.isInteger(Number(i)) ? Number(i) : i

export const isActive = res => {
    res.sig = convertToInt(res.sig)
    if (Number.isInteger(res.sig)) {
        res.active = true
    }
}

export const parseSignal = res => {
    isActive(res)
    if (res.active) return
    const {sig} = res
    res.a = sig
    if (sig.includes('AND') || sig.includes('OR')) {
        const [_, a, op, b] = sig.match(/([\d\w]*) (AND|OR) ([\d\w]*)/)
        res.op = op
        res.a = convertToInt(a)
        res.b = convertToInt(b)
        res.calc = (a, b) => op === 'AND' ? a&b : a|b
    }
    if (sig.includes('LSHIFT') || sig.includes('RSHIFT')) {
        const [_, a, op, b] = sig.match(/([\d\w]*) (LSHIFT|RSHIFT) ([\d]*)/)
        res.op = op
        res.a = convertToInt(a)
        res.b = Number(b)
        res.calc = (a, b) => op === 'LSHIFT' ? a << b : a >> b
    }
    if (sig.includes('NOT')) {
        const [_, a] = sig.match(/NOT ([\d\w]*)/)
        res.op = 'NOT'
        res.a = convertToInt(a)
        res.calc = a => MAX_HEX_VALUE-a
    }
}

const connectWires = res => {
    if (!res.op && Number.isInteger(wires[res.a])) {
        return wires[res.wire] = wires[res.a]
    }
    if (!res.b) {
        if (Number.isInteger(res.a)) {
            return wires[res.wire] = res.calc(res.a)
        }
        if (Number.isInteger(wires[res.a])) {
            return wires[res.wire] = res.calc(wires[res.a])
        }
    } else {
        if (Number.isInteger(res.b)) {
            if (Number.isInteger(res.a)) {
                return wires[res.wire] = res.calc(res.a, res.b)
            }
            if (Number.isInteger(wires[res.a])) {
                return wires[res.wire] = res.calc(wires[res.a], res.b)
            }
        }
        if (Number.isInteger(wires[res.b])) {
            if (Number.isInteger(res.a)) {
                return wires[res.wire] = res.calc(res.a, wires[res.b])
            }
            if (Number.isInteger(wires[res.a])) {
                return wires[res.wire] = res.calc(wires[res.a], wires[res.b])
            }
        }
    }
}

const processInstructions = instructions => {
    instructions.forEach(i => {
        const res = parseInstruction(i)
        parseSignal(res)
        if (res.active && !wires[res.wire]) {
            wires[res.wire] = res.sig
        } else {
            connectWires(res)
        }
    })
}

const isCircuitComplete = instructions => {
    const wiresCount = Object.keys(wires).length
    return instructions.length === wiresCount
}

const instructions = input.split('\n')

while (!isCircuitComplete(instructions)) {
    processInstructions(instructions)
}

const p1 = wires['a']
console.log(p1)
resetWires()
wires['b'] = p1

while (!isCircuitComplete(instructions)) {
    processInstructions(instructions)
}

console.log(wires['a'])
