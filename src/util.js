import fs from 'fs'
export const input = fs.readFileSync(0).toString('utf-8')

export const sum = arr => arr.reduce((acc, i) => acc+Number(i), 0)
