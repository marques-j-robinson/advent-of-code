import fs from 'fs'

export const input = fs.readFileSync(0).toString('utf-8').trim()

export const splitBy = (str, type) => str.split(type)
